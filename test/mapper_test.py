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

    def test_date(self):
        event = Event()
        now = datetime.now()
        event.date = now
        assert Mapper.to_row(event)['date'] == now

    def test_enrollment_date(self):
        event = Event()
        now = datetime.now()
        event.enrollment_date = now
        assert Mapper.to_row(event)['enrollment_date'] == now

class TestMapperToEvent(TestCase):

    def setUp(self):
        self.row = {
            'id': None,
            'title': False,
            'date': None,
            'enrollment_date': None,
            'notification_sent': False
        }

    def test_maps_id_to_event(self):
        self.row['id'] = 'online-uid232@online.no'
        assert Mapper.to_event(self.row).id == 'online-uid232@online.no'

    def test_notification_status_to_event(self):
        self.row['notification_sent'] = True
        assert Mapper.to_event(self.row).notification_sent == True

    def test_maps_title_to_event(self):
        self.row['title'] = 'Cool event'
        assert Mapper.to_event(self.row).title == 'Cool event'

    def test_maps_date_to_event(self):
        now = datetime.now() 
        self.row['date'] = now
        assert Mapper.to_event(self.row).date == now

    def test_maps_enrollment_date_to_event(self):
        now = datetime.now() 
        self.row['enrollment_date'] = now
        assert Mapper.to_event(self.row).enrollment_date == now
