from unittest import TestCase, skip
from unittest.mock import patch, MagicMock
from channels import Facebook

class TestFacebook(TestCase):

    @patch('channels.facebook.fbchat')
    def test_connects_when_message_should_be_sent(self, fbchat):
        event = MagicMock()
        Facebook().notify(event)
        assert fbchat.Client.called

    @patch('channels.facebook.fbchat')
    def test_event_gets_marked_as_sent(self, fbchat):
        event = MagicMock()
        Facebook().notify(event)
        assert event.notification_sent == True
