from feeds.feed import Feed
from event import Event
from datetime import datetime

class Online(Feed):

    host = 'https://online.tefewffenu.no'
    feed = '/events/search/?query=&future=true&myevents=false'

    def fetch_html(self):
        return self.download(self.host + self.feed)

    def parse_events(self, html):
        html_events = self.selector(html, 'article.row')
        return [self.convert_event(html_event) \
            for html_event in html_events]

    def extract_date(self, html_event):
        html_date = html_event.select('.left-box')[0].parent['data-date']
        colons_removed = ''.join(html_date.rsplit(':', 1)).strip()
        date = datetime.strptime(colons_removed, '%Y-%m-%dT%H:%M:%S%z')
        return date.replace(tzinfo=None)

    def extract_enrollment_date(self, html_event):
        html_date = html_event.select('.col-md-5')
        if html_date:
            stripped_date = html_date[0].text.strip()
            date_format = 'Påmelding åpner %d.%m.%y %H.%M'
            return datetime.strptime(stripped_date, date_format)

    def extract_title(self, html_event):
        return html_event.select('h1')[0].text.strip()

    def convert_event(self, html_event):
        event = Event()
        event.title = self.extract_title(html_event)
        event.date = self.extract_date(html_event)
        event.enrollment_date = self.extract_enrollment_date(html_event)
        return event

    def get_events(self):
        html = self.fetch_html()
        events = self.parse_events(html) \
            if html else []
        return events
