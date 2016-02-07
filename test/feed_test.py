from unittest import TestCase
from unittest.mock import patch, MagicMock
from requests import RequestException
from feeds.feed import Feed

def connection_error(*args, **kwargs):
    raise RequestException

class TestFeed(TestCase):

    @patch('feeds.feed.log')
    @patch('feeds.feed.Fetcher')
    def test_logs_connection_errors_when_download_fails(self, fetcher, log):
        fetcher.get = MagicMock(side_effect=connection_error)
        Feed().download('http://feed.url.com/events')
        assert log.warning.called

    @patch('feeds.feed.log')
    @patch('feeds.feed.Selector')
    def test_logs_selector_misses_when_no_match_found(self, Selector, log):
        Selector.find.return_value = []
        Feed().selector('<h1>Hello world</h1>', 'h2')
        assert log.warning.called
