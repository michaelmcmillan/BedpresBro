class Event:

    def __init__(self):
        self.id = None
        self.title = None
        self.date = None
        self.enrollment_date = None
        self.notification_sent = False

    def __eq__(self, other):
        return self.id == other.id
