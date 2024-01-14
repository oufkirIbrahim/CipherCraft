import os
import time
from sys import stderr
from colorama import Fore, Style, init
from .errorLogger import ErrorLogger


class LogoHandler:
    def __init__(self):
        init()
        self.error_logger = ErrorLogger()

    def print_ascii_art(self):
        try:
            # LOAD LOGO PATH
            logo_path = os.path.join(os.path.dirname(__file__), 'files', 'logo.txt')

            # TRY TO READ ASCII ART FROM FILE
            with open(logo_path, 'r') as file:
                color_counter = 0

                # LOOPING THE FILE
                for line in file:

                    # Alternate colors between cyan and magenta
                    color = Fore.CYAN if color_counter % 2 == 0 else Fore.MAGENTA
                    colored_line = f'{color}{line}{Style.RESET_ALL}'
                    print(colored_line, end='', flush=True)  # flush=True ensures immediate output

                    # Increment color counter
                    color_counter += 1

                    # Add a sleep effect for visualization (50 milliseconds in this example)
                    time.sleep(0.05)
                print()

        except Exception as e:
            # SOMETHING WENT WRONG
            stderr.write(f'Error: {e}')
            self.error_logger.error_log(e)


# EXAMPLE USAGE:
if __name__ == "__main__":
    logo = LogoHandler()
    logo.print_ascii_art()
