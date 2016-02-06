from .feed import Feed
from event import Event
from datetime import datetime, timedelta
import time

class Stdin(Feed):

    def get_events(self):
        event = Event()
        event.id = 'unique'
        event.title = 'Øl øl øl!'
        event.notification_sent = False
        event.date = datetime.now() + timedelta(days=1)
        event.enrollment_date = datetime.now() + timedelta(minutes=10)
        time.sleep(5)
        return [event]
