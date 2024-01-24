from .eventsHandler import EventsHandler


class LogsHandler:
    def __init__(self):
        self.eventsHandler = EventsHandler()

    def log_event(self, msg):

        # LOG THE EVENTS TO LOG FILE
        self.eventsHandler.add_event(msg, 'logs.txt')
