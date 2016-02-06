class Event:

    def __init__(self):
        self.id = None
        self.notified = False
        self.title = None
        self.date = None
        self.enrollment_date = None
        self.location = None
        self.queued = 0
        self.enrolled = 0
        self.notification_sent = False

    def __eq__(self, other):
        return self.id == other.id
