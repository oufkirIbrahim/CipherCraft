from .eventsHandler import EventsHandler


class ErrorLogger:
    def __init__(self):
        self.eventsHandler = EventsHandler()

    def error_log(self, msg):

        # LOG THE ERROR INTO ERROR LOGS FILE
        self.eventsHandler.add_event(msg, 'errorLogs.txt')
