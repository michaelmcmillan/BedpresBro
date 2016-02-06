import threading
from bro import Bro
from brain import Brain
from logger import log
from feeds import Online
from channels import Facebook

if __name__ == '__main__':

    print(r'''
     o©ºº©oo©oº°©           
    /           \          
    |___________|____      
    |            |____)     
    |   B E D    |  | |     
    |            |  | |     
    |  P R  E S  |  | |     
    |            |  | |     
    |   B R O    |  | |     
    |            |__|_|     
    |            |____)     
    |____________|          
   (______________)        
    ''')

    bro = Bro()
    bro.feeds = [Online()]
    bro.channels = [Facebook()]

    # Setup memory if it does not exist
    Brain.setup()

    # Pull events from feeds every 30 minutes
    def pull_events():
        log.info('Pulling events from %d feed(s).' % len(bro.feeds))
        bro.pull_events_from_feeds()
        threading.Timer(60 * 30, pull_events).start()

    # Push events to channel every 10 seconds
    def push_events():
        log.info('Pushing events to %d channel(s).' % len(bro.channels))
        bro.push_events_to_channels()
        threading.Timer(10.0, push_events).start()

    # Kick off pull and push threads
    pull_events()
    push_events()
