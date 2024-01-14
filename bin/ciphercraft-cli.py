import os
import sys
import questionary
from colorama import Fore, Style, init

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CipherCraft.utils.Generators.logoHandler import LogoHandler
import CipherCraft.utils.enums.preference as pr
from CipherCraft.utils.filesHandler import FilesHandler
from CipherCraft.utils.Runner import Runner


class CLInterface:

    def __init__(self):
        self.logo_handler = LogoHandler()
        self.files_handler = FilesHandler()
        self.runner = Runner()
        self.preference = {
            'action': None,
            'algorithm': None,
            'operation': None,
            'key_selection': {
                'encryption': {
                    'call': None,
                    pr.EncryptionKey.IMPORT_KEY.__name__(): self.import_key,
                    pr.EncryptionKey.INPUT_KEY.__name__(): self.input_key,
                    pr.EncryptionKey.GENERATE_RANDOM_KEY.__name__(): self.generate_key,
                },
                'decryption': {
                    'call': None,
                    pr.DecryptionKey.IMPORT_KEY.__name__(): self.import_key,
                    pr.DecryptionKey.INPUT_KEY.__name__(): self.input_key,
                    pr.DecryptionKey.WITHOUT_KEY.__name__(): self.perform_cryptanalysis,
                },
            },
            'key': None,
            'cryptanalysis': None,
            'source_selection': {
                'call': None,
                pr.InputMethod.INPUT.__name__(): self.get_source_stdin,
                pr.InputMethod.IMPORT_FROM_FILE.__name__(): self.get_source_file
            },
            "source": None,
            'dist_selection': {
                'call': None,
                pr.OutputMethod.PRINT_ONLY.__name__(): self.print_dist_stdout,
                pr.OutputMethod.SAVE_TO_FILE.__name__(): self.print_dist_file
            },
            "dist": None,
            "dist_path": None
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_logo(self):
        self.clear_screen()
        self.logo_handler.print_ascii_art()

    def get_user_choice(self, prompt, choices):
        """
        This Function Prompts The User For Choice Selection
        :param prompt:
        :param choices:
        :return: None
        """
        return questionary.select(prompt, choices=[_['name'] for _ in choices]).ask()

    def get_text_input(self, prompt):
        return questionary.text(prompt).ask()

    def get_confirmation(self, prompt):
        return questionary.confirm(prompt).ask()

    def algorithm_handler(self, algorithms):

        """
        THis Function Handles Algorithm Selection
        :param algorithms:
        :return: None
        """
        self.preference['algorithm'] = self.get_user_choice(
            "Select an algorithm:",
            choices=algorithms.choices()
        )

    def operation_handler(self, operations):

        """
        THis Function Handles Cryptography Actions -Encrypt or -Decrypt
        :param operations:
        :return: None
        """
        self.preference['operation'] = self.get_user_choice(
            "Select an operation:",
            choices=operations.choices()
        )
        return

    def stream_actions(self, stream_type='source'):
        """
        This Function Execute The Corresponding Actions On Streams
        :param stream_type:
        :return:
        """

        # EXECUTING THE CORRESPONDING FUNCTION ON STREAM
        index = self.preference[f'{stream_type}_selection']['call']
        self.preference[f'{stream_type}_selection'][index]()

    def streams_handler(self, p):
        """
        This Function Handles Stream Input/ Output Sourcing
        :param p:
        :return:
        """

        # SELECT THE INPUT AND OUTPUT NAMING AND GET DATA SOURCE
        if pr.Operations.ENCRYPT.__cmp__(self.preference['operation']):
            self.stream_handler(p.InputMethod, 'source', 'plaintext')
            self.stream_actions('source')
            self.stream_handler(p.OutputMethod, 'dist', 'ciphertext', ' destination')
            self.stream_actions('dist')
        else:
            self.stream_handler(p.InputMethod, 'source', 'ciphertext')
            self.stream_actions('source')
            self.stream_handler(p.OutputMethod, 'dist', 'ciphertext', ' destination')
            self.stream_actions('dist')

    def classic_handler(self, p: pr):
        """
        This Function Handles The Classic Algorithms Logic
        :param p:
        :return: None
        """

        # SELECT THE DESIRED ALGORITHM
        self.algorithm_handler(p.ClassicAlgorithms)

        # SELECT THE DESIRED OPERATION
        self.operation_handler(p.Operations)

        # HANDLE STREAMS
        self.streams_handler(p)

        # HANDLING THE KEY
        self.key_handler(p)

    def modern_handler(self, p: pr):
        """
        This Function Handles The Modern Algorithms Logic
        :param p:
        :return: None
        """

        # SELECT THE DESIRED ALGORITHM
        self.algorithm_handler(p.ModernAlgorithms)

        # SELECT THE DESIRED OPERATION
        self.operation_handler(p.Operations)

        # HANDLE STREAMS
        self.streams_handler(p)

        # HANDLING THE KEY
        self.key_handler(p)

    def stream_handler(self, p, stream_type="source", text_type="plaintext", alt=""):
        """
        This Function handles The Source OF Streams
        :param stream_type:
        :param alt:
        :param p:
        :param text_type:
        :return:
        """

        # SELECT THE SOURCE OF INPUT DATA
        self.preference[stream_type + '_selection']['call'] = self.get_user_choice(
            f'Select {text_type}{alt} source:',
            choices=p.choices()
        )
        return

    def key_selection_handler(self, p: pr, action='encryption'):
        """
        This Function Handles The Key Selection
        :param action:
        :param p:
        :return: None
        """
        self.preference['key_selection'][action]['call'] = self.get_user_choice(
            "Select a Key:",
            choices=p.choices()
        )

    def key_handler(self, p: pr):
        """
        This Function Perform Different Actions On Keys
        :param p:
        :return: None
        """

        # CHECK IF THE USER HAS SELECTED TO PROCEED WITHOUT DECRYPTION KEY
        if pr.DecryptionKey.WITHOUT_KEY.__cmp__(self.preference['key_selection']['decryption']['call']):
            # NOTHING TO DO
            return
        # SELECT THE KEY METHOD
        if pr.Operations.ENCRYPT.__cmp__(self.preference['operation']):

            # ENCRYPTION
            self.key_selection_handler(p.EncryptionKey, 'encryption')

            # GET THE KEY INDEX
            index = self.preference['key_selection']['encryption']['call']

            # CALL THE CORRESPONDING FUNCTION
            self.preference['key_selection']['encryption'][index]()

        else:
            # DECRYPTION
            self.key_selection_handler(p.DecryptionKey, 'decryption')

            # GET THE KEY INDEX
            index = self.preference['key_selection']['decryption']['call']

            # CALL THE CORRESPONDING FUNCTION
            self.preference['key_selection']['decryption'][index]()

    def input_key(self):
        """
        This Function Gets The Key From STDIN
        :return:
        """

        self.preference['key'] = self.get_text_input("Key:")
        return

    def import_key(self):
        """
        This Function Imports The Key From Files
        :return:
        """
        self.import_file('key')

    def import_file(self, name):
        """
        This Function Imports Files
        :param name:
        :return:
        """
        # GETTING THE SOURCE PATH
        file_path = self.get_text_input(f"Path to the key {name}:")

        content = None
        # CHECKING THE SOURCE PATH VALIDATION
        if os.path.exists(file_path) and os.path.isfile(file_path):
            content = self.files_handler.read_file(file_path)

            # CHECKING IF CONTENT IS SET PROPERLY
            if content is not None:
                # CONTENT IS VALID
                self.preference[name] = content
            else:
                print('File is Empty')
                # REDO
                self.import_file(name)
        else:
            print('Path not valid')
            # REDO
            self.import_file(name)

        return

    def generate_key(self):
        """

        :return:
        """
        return

    def perform_cryptanalysis(self):
        """
        This Function Selects The Cryptanalysis Method To Decrypt
        :return:
        """
        self.preference['cryptanalysis'] = self.get_user_choice(
            "Select a cryptanalysis algorithm :",
            choices=pr.CryptAnalysis.choices()
        )

    def get_source_stdin(self, source_type='plaintext'):
        """
        This Function Gets Source Data From STDIN
        :return:
        """
        self.preference["source"] = self.get_text_input(f"Source {source_type}:")
        return

    def get_source_file(self):
        """
        This Function Imports Source Data From Files
        :return:
        """

        self.import_file('source')

    def print_dist_stdout(self):
        """

        :return:
        """

        # CHECKS IF THE OUTPUT IS SET
        if self.preference['dist'] is not None:
            print(f"Output: {self.preference['dist']}")
        else:
            print('Not yet')
            # <--------------------------------------- Needs Attention <-----------------------------------

    def print_dist_file(self):
        """
        This Function Handles The Output Stream Sourcing
        :return:
        """
        if self.preference['dist_path'] is None:

            # GETTING THE DESTINATION PATH
            file_dist = self.get_text_input("Path to the save the output:")

            # GETTING THE FILE DIRECTORY
            file_path = os.path.dirname(file_dist)

            # GETTING THE FILE NAME
            file_name = os.path.basename(file_dist)

            # TESTING THE VALIDATION : PATH EXISTS AND NOT A DIRECTORY
            if os.path.exists(file_path) and not os.path.isdir(file_dist):

                # CHECKING IF THE FILE NAME ALREADY EXISTS
                if os.path.isfile(file_dist):
                    print(f'file {file_name} already exists!')
                    # REDO
                    self.print_dist_file()
                else:
                    # SETTING THE DESTINATION PATH
                    self.preference['path_dist'] = file_dist
            else:
                print('Path is not valid!')
                # REDO
                self.print_dist_file()

        else:

            status = False
            status = self.files_handler.write_file(self.preference['dist_path'], self.preference['dist'])

            # CHECKING THE STATUS
            if not status:
                # CONTENT IS VALID
                print('File is Empty')

                # MORE ACTIONS HERE <-----------------------------------------
                self.print_dist_file()
                # <------------------------------------------------------------
            else:
                print(f'Saved To: {self.preference["dist_path"]}')

        return

    def main_menu(self):

        while True:
            self.print_logo()
            self.preference['action'] = self.get_user_choice(
                "Select an option:",
                choices=pr.Actions.choices()
            )

            # TESTING CHOICE
            if pr.Actions.EXIT.__cmp__(self.preference['action']):

                # EXITING THE PROGRAM
                sys.exit(0)
            elif pr.Actions.CLASSIC.__cmp__(self.preference['action']):

                # CHOOSE A CLASSIC ALGORITHM
                self.classic_handler(pr)
            elif pr.Actions.MODERN.__cmp__(self.preference['action']):
                # CHOOSE A MODERN ALGORITHM
                self.modern_handler(pr)

            # PERFORM ACTIONS
            self.run_app()

    def run_app(self):
        """This Function Runs The Actions"""
        self.preference['dist'] = self.preference['dist'] = self.runner.run(
            self.preference['action'],
            self.preference['algorithm'],
            self.preference['operation'],
            self.preference['source'],
            self.preference['key'])

        self.print_out_stream()
        return

    def print_out_stream(self):
        init(autoreset=True)  # Initialize colorama

        self.print_logo()
        print("\n", Fore.GREEN + Style.BRIGHT + "Processing...")

        print(Fore.CYAN + Style.BRIGHT + "\nSelected Options:")
        print(f"{Fore.YELLOW + Style.BRIGHT}Action: {self.preference['action']}")
        print(f"{Fore.YELLOW + Style.BRIGHT}Algorithm: {self.preference['algorithm']}")
        print(f"{Fore.YELLOW + Style.BRIGHT}Operation: {self.preference['operation']}")
        print(f"{Fore.YELLOW + Style.BRIGHT}Key: {self.preference['key']}")
        print(f"{Fore.YELLOW + Style.BRIGHT}Input text: {self.preference['source']}")
        print(f"{Fore.YELLOW + Style.BRIGHT}Output text: {self.preference['dist']}")
        print(f"{Fore.YELLOW + Style.BRIGHT}Save path: {self.preference['dist_path']}")
        print("\n" + Fore.GREEN + Style.BRIGHT + "Process Completed!")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    cli_interface = CLInterface()
    cli_interface.main_menu()
    cli_interface.print_out_stream()
