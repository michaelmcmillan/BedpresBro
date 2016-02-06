from unittest import TestCase, skip
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from bro import Bro

in_one_day = datetime.now() + timedelta(days=1)
one_day_ago = datetime.now() - timedelta(days=1)
in_one_hour = datetime.now() + timedelta(hours=1)
in_fifteen_minutes = datetime.now() + timedelta(minutes=15)

class TestBro(TestCase):

    @patch('bro.Brain')
    def test_finds_event_with_enrollment_within_twenty_minutes(self, brain):
        event = MagicMock(enrollment_date=in_fifteen_minutes, notification_sent=False)
        brain.all.return_value = [event]
        assert Bro().whats_enrolling() == [event]

    @patch('bro.Brain')
    def test_ignores_event_with_enrollment_in_one_hour(self, brain):
        event = MagicMock(enrollment_date=in_one_hour, notification_sent=False)
        brain.all.return_value = [event]
        assert Bro().whats_enrolling() == []

    @patch('bro.Brain')
    def test_ignores_event_thats_already_notified(self, brain):
        event = MagicMock(enrollment_date=in_fifteen_minutes, notification_sent=True)
        brain.all.return_value = [event]
        assert Bro().whats_enrolling() == []

    def test_event_without_enrollment_date_from_feed_gets_ignored(self):
        lacking_event = MagicMock(enrollment_date=None)
        feed = MagicMock()
        feed.get_events.return_value = [lacking_event]
        assert Bro(feeds=[feed]).look_for_future_events() == []

    def test_event_in_past_from_feed_gets_ignored(self):
        old_event = MagicMock(enrollment_date=one_day_ago)
        feed = MagicMock()
        feed.get_events.return_value = [old_event]
        assert Bro(feeds=[feed]).look_for_future_events() == []

    def test_event_in_future_from_feed_gets_returned(self):
        new_event = MagicMock(enrollment_date=in_one_day)
        feed = MagicMock()
        feed.get_events.return_value = [new_event]
        assert Bro(feeds=[feed]).look_for_future_events() == [new_event]
    
    @patch('bro.Bro.look_for_future_events')
    @patch('bro.Brain')
    def test_future_events_get_passed_onto_brain(self, brain, future_events):
        future_event = MagicMock(enrollment_date=in_one_day)
        future_events.return_value = [future_event]
        Bro().pull_events_from_feeds()
        brain.create.assert_called_with(future_event)

    @patch('bro.Bro.whats_enrolling')
    def test_enrolling_events_get_passed_onto_channels(self, whats_enrolling):
        enrolling_event = MagicMock(id='id', title='title',  enrollment_date=in_fifteen_minutes)
        whats_enrolling.return_value = [enrolling_event]
        facebook = MagicMock()
        Bro(channels=[facebook]).push_events_to_channels()
        facebook.notify.assert_called_with(enrolling_event)
