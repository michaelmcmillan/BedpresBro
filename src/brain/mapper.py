from event import Event

class Mapper:

    @classmethod
    def to_row(cls, event):
        row = {}
        row['id'] = event.id
        row['title'] = event.title
        row['date'] = event.date
        row['enrollment_date'] = event.enrollment_date
        row['notification_sent'] = event.notification_sent
        return row

    @classmethod
    def to_event(cls, row):
        event = Event()
        if row['id']:
            event.id = row['id']
        if row['title']:
            event.title = row['title']
        if row['notification_sent']:
            event.notification_sent = row['notification_sent']
        if row['date']:
            event.date = row['date']
        if row['enrollment_date']:
            event.enrollment_date = row['enrollment_date']
        return event
