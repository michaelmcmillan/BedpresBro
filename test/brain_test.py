from unittest import TestCase, skip
from unittest.mock import patch, MagicMock
from datetime import datetime
import sqlite3
from brain import Brain
from event import Event

class TestBrain(TestCase):

    def setUp(self):
        Brain.connection = sqlite3.connect(':memory:')
        Brain.setup()
        self.event = MagicMock(
            id='223-unique-id',
            title='Cool event',
            enrollment_date=datetime.now(),
            date=datetime.now(),
            notification_sent = False
        )

    def test_saves_event_if_event_is_not_already_stored(self):
        Brain.create(self.event)
        stored_event = Brain.read('223-unique-id')
        assert stored_event.title == 'Cool event'
        assert stored_event.notification_sent == False
        assert str(stored_event.date) == str(self.event.date)
        assert str(stored_event.enrollment_date) == str(self.event.enrollment_date)

    def test_rejects_event_if_event_is_already_stored(self):
        Brain.create(self.event)
        Brain.create(self.event)
        assert len(Brain.all()) == 1

    def test_can_update_event(self):
        Brain.create(self.event)
        self.event.title = 'Updated event'
        Brain.update(self.event)
        assert Brain.read('223-unique-id').title == 'Updated event'
