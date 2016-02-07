from logger import log
from requests import RequestException
from .fetcher import Fetcher
from .selector import Selector

class Feed:

    def download(self, url):
        try:
            Fetcher.get(url)
        except RequestException as e:
            log.warning('Could not connect to %s.' % url, e)

    def selector(self, html, css_selector):
        matches = Selector.find(html, css_selector)
        if not matches:
            log.warning('Selector did not match anything: %s' % css_selector)
        return matches

    def get_events(self):
        pass
