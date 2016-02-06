from datetime import datetime, timedelta
from brain import Brain

class Bro:

    def __init__(self, feeds=None, channels=None):
        self.feeds = feeds or []
        self.channels = channels or []

    # Input: Feeds
    def look_for_future_events(self):
        new_events = []
        now = datetime.now()
        for feed in self.feeds:
            new_events += [event for event in feed.get_events() \
                if event.enrollment_date
                and event.enrollment_date > now]
        return new_events

    # Input: Database
    def pull_events_from_feeds(self):
        future_events = self.look_for_future_events()
        for future_event in future_events:
            Brain.create(future_event)

    # Output: Database
    def whats_enrolling(self):
        twenty_minutes_from_now = datetime.now() + timedelta(minutes=20)
        return [event for event in Brain.all() \
            if event.enrollment_date
            and event.enrollment_date < twenty_minutes_from_now
            and event.notification_sent is False]

    # Output: Channels
    def push_events_to_channels(self):
        enrolling_events = self.whats_enrolling()
        for enrolling_event in enrolling_events:
            for channel in self.channels:
                channel.notify(enrolling_event)
                Brain.update(enrolling_event)
