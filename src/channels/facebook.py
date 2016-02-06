import fbchat
from config import configuration

class Facebook:

    def __init__(self):
        username = configuration['facebook']['username']
        password = configuration['facebook']['password']
        self.client = fbchat.Client(username, password)
        self.thread = configuration['facebook']['message_thread']

    def notify(self, event):
        self.client.send(self.thread, event.title)
        event.notification_sent = True
