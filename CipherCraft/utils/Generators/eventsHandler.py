from datetime import datetime
from sys import stderr
from uuid import uuid4 as uuid
import os


class EventsHandler:

    @staticmethod
    def add_event(msg, filename):
        """

        :param msg:
        :param filename:
        :return: @None
        """
        # DATETIME FORMAT
        date_time = datetime.now().strftime("%Y-%m-%d\t%H:%M:%S")

        # LOG ITEM
        log_item = f'{date_time}\t{uuid()}\t{msg}'
        try:
            # SELECT THE LOGS DIR
            path_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'logs')
            if not os.path.exists(path_dir):
                # CREATES NEW ONE
                os.makedirs(path_dir)

            # THE LOG FILE PATH
            log_file = os.path.join(path_dir, filename)

            # OPEN FILE PATH IN APPEND MODE
            with open(log_file, 'a') as file:

                # APPEND THE LOG ITEM TO THE LOG FILE
                file.write(log_item + "\n")

        except Exception as e:
            # SOMETHING WENT WRONG
            stderr.write(f'Error: {e}')



