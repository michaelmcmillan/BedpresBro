from unittest import TestCase, skip
from datetime import datetime, timedelta
from event import Event
from brain.mapper import Mapper

class TestMapperToRow(TestCase):

    def test_maps_id(self):
        event = Event()
        event.id = 'online-uid232@online.no'
        assert Mapper.to_row(event)['id'] == 'online-uid232@online.no'

    def test_notification_status(self):
        event = Event()
        event.notification_sent = True
        assert Mapper.to_row(event)['notification_sent'] == True

    def test_notification_status(self):
        event = Event()
        event.title = 'Cool title'
        assert Mapper.to_row(event)['title'] == 'Cool title'

class TestMapperToEvent(TestCase):

    def test_maps_id_to_event(self):
        row = {'id': 'online-uid232@online.no', 'title': False, 'notification_sent': False}
        assert Mapper.to_event(row).id == 'online-uid232@online.no'

    def test_notification_status_to_event(self):
        row = {'id': False, 'title': False, 'notification_sent': True}
        assert Mapper.to_event(row).notification_sent == True

    def test_maps_title_to_event(self):
        row = {'id': False, 'title': 'Cool event', 'notification_sent': False}
        assert Mapper.to_event(row).title == 'Cool event'
