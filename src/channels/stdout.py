class Stdout:

    def __init__(self):
        pass

    def notify(self, event):
        print("Asked to send this event:")
        print(event.title)
        event.notification_sent = True
