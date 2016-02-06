from event import Event

class Mapper:

    @classmethod
    def to_row(cls, event):
        row = {}
        if event.id:
            row['id'] = event.id
        if event.title:
            row['title'] = event.title
        if event.date:
            row['date'] = event.date
        if event.enrollment_date:
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
