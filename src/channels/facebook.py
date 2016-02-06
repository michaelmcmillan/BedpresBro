import fbchat
from config import configuration

class Facebook:

    def __init__(self):
        self.username = configuration['facebook']['username']
        self.password = configuration['facebook']['password']
        self.thread = configuration['facebook']['message_thread']

    def notify(self, event):
        client = fbchat.Client(self.username, self.password)
        client.send(self.thread,
            'Påmelding til "%s" begynner om under 20 minutter.' % event.title
        )
        event.notification_sent = True
