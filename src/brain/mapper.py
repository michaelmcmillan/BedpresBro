from event import Event

class Mapper:

    @classmethod
    def to_row(cls, event):
        return {
            'id': event.id,
            'title': event.title,
            'notification_sent': event.notification_sent
        }

    @classmethod
    def to_event(cls, row):
        event = Event()
        if row['id']:
            event.id = row['id']
        if row['title']:
            event.title = row['title']
        if row['notification_sent']:
            event.notification_sent = row['notification_sent']
        return event
