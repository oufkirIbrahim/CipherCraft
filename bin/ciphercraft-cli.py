import os
import sys
import time
import questionary
from colorama import Fore, Style, init
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CipherCraft.utils.Generators.logoHandler import LogoHandler

init(autoreset=True)

class CLInterface:

    actions = {
        'select_action': {
            'Classic': '',
            'Modern': '',
            'Exit': ''
        },
        'select_function': {
            'Encrypt': '',
            'Decrypt': '',
        },
        'select_classic': {
            'Caesar': '',
            'Affine': '',
            'Vigenere': '',
            'Multiplicative': ''
        },
        'select_modern': {
            'AES':''
        }
    }

    def __init__(self):
        self.logo_handler = LogoHandler()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_logo(self):
        self.clear_screen()
        # Call the print_ascii_art method from LogoHandler to display the logo
        self.logo_handler.print_ascii_art()

    def get_user_choice(self, prompt, choices):
        return questionary.select(prompt, choices=choices).ask()

    def get_text_input(self, prompt):
        return questionary.text(prompt).ask()

    def get_confirmation(self, prompt):
        return questionary.confirm(prompt).ask()

    def main_menu(self):
        while True:
            self.print_logo()
            choice = self.get_user_choice(
                "Select an option:",
                choices=["Classic", "Modern", "Exit"]
            )

            if choice == "Exit":
                sys.exit(0)

            crypto_algo = self.get_user_choice(
                "Select a cryptographic algorithm:",
                choices=["Caesar", "Vigenere"]
            )

            action = self.get_user_choice(
                "Select an action:",
                choices=["Encrypt", "Decrypt"]
            )

            key = self.get_text_input("Enter the key:")

            if action == "Encrypt":
                message_or_path = self.get_text_input("Enter the message:")
            else:
                message_or_path = self.get_text_input("Enter the path to the encrypted file:")

            save_location_or_stream = self.get_text_input("Enter the save location or output stream:")

            printing_option = self.get_confirmation("Print the result?")

            # Perform encryption/decryption logic here
            # For simplicity, let's just print the inputs for demonstration
            self.print_logo()
            print("\n", Fore.GREEN + Style.BRIGHT + "Processing...")
            print(Fore.CYAN + Style.BRIGHT + f"\nSelected Options:")
            print(f"Crypto Algorithm: {crypto_algo}")
            print(f"Action: {action}")
            print(f"Key: {key}")
            print(f"Message/Path: {message_or_path}")
            print(f"Save Location/Stream: {save_location_or_stream}")
            print(f"Print Result: {'Yes' if printing_option else 'No'}")
            print("\n" + Fore.GREEN + Style.BRIGHT + "Process Completed!")

            input("\nPress Enter to continue...")

if __name__ == "__main__":
    cli_interface = CLInterface()
    cli_interface.main_menu()
