from unittest import TestCase, skip
from unittest.mock import patch, MagicMock
import sqlite3
from brain import Brain
from event import Event

class TestBrain(TestCase):

    def setUp(self):
        Brain.connection = sqlite3.connect(':memory:')
        Brain.setup()

    def test_saves_event_if_event_is_not_already_stored(self):
        event = MagicMock(id='223-unique-id', title='Cool event')
        Brain.create(event)
        stored_event = Brain.read('223-unique-id')
        assert stored_event.title == 'Cool event'

    def test_rejects_event_if_event_is_already_stored(self):
        event = MagicMock(id='event-229@online.ntnu.no', title='Old event')
        Brain.create(event)
        Brain.create(event)
        assert Brain.all() == [event]

    def test_can_update_event(self):
        event = MagicMock(id='event-229@online.ntnu.no', title='Old event')
        Brain.create(event)
        event.title = 'Updated event'
        Brain.update(event)
        assert Brain.read('event-229@online.ntnu.no').title == 'Updated event'
