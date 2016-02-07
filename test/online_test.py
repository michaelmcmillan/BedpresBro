from unittest import TestCase, skip
from unittest.mock import patch, MagicMock
from datetime import datetime
from feeds.formulas import Online
from test.fixtures.online_bedpres_html_event import fixture

class TestBro(TestCase):

    @patch('feeds.formulas.online.Online.fetch_html')
    def test_returns_no_events_if_empty_response(self, fetch_html):
        fetch_html.return_value = None
        events = Online().get_events()
        assert events == []

    @patch('feeds.formulas.online.Online.fetch_html')
    def test_extracts_event_title_from_html(self, fetch_html):
        fetch_html.return_value = fixture
        event = Online().get_events()[0]
        assert event.title == 'KiD - Internet of Things'

    @patch('feeds.formulas.online.Online.fetch_html')
    def test_extracts_event_date_from_html(self, fetch_html):
        fetch_html.return_value = fixture
        event = Online().get_events()[0]
        assert event.date == datetime(2016, 2, 1, 17)

    @patch('feeds.formulas.online.Online.fetch_html')
    def test_extracts_event_enrollment_date_from_html(self, fetch_html):
        fetch_html.return_value = fixture
        event = Online().get_events()[0]
        assert event.enrollment_date == datetime(2016, 1, 25, 12)
