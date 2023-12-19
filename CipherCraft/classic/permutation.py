import random


class PermutationCipher:
    def __init__(self, key=None):
        # Define the alphabet for the cipher
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # If no key is provided, generate a random key
        if key is None:
            key = self.generate_random_key()

        # Validate the key
        if len(key) != len(self.alphabet) or sorted(key) != list(self.alphabet):
            raise ValueError("The permutation key must contain all alphabet letters without repetition.")

        # Store the key as an attribute of the class
        self.key = key

    def generate_random_key(self):
        # Generate a random permutation of the alphabet
        shuffled_alphabet = list(self.alphabet)
        random.shuffle(shuffled_alphabet)
        return ''.join(shuffled_alphabet)

    def encrypt(self, text):
        # Encrypt the input text using the permutation key
        encrypted_text = ''
        for char in text:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encrypted_text += self.key[index]
            else:
                encrypted_text += char

        return encrypted_text

    def decrypt(self, text):
        # Decrypt the input text using the inverse of the permutation key
        decrypted_text = ''
        for char in text:
            if char in self.alphabet:
                index = self.key.index(char)
                decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char

        return decrypted_text
