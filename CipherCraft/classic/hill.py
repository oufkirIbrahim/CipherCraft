import numpy as np
import sympy


class HillCipher:
    def __init__(self, key):
        self.key = key

    def pad_plain_text(self, plain_text):
        # Pad the plain text if its length is not a multiple of the key matrix size
        padding_length = len(self.key) - (len(plain_text) % len(self.key))
        return plain_text + 'X' * padding_length

    def matrix_inverse_mod(self, modulus=26):
        M = sympy.Matrix(self.key)
        determinant = M.det() % 26  # huge intermediate results/crashes
        inverse = M.inv_mod(26)
        return inverse

    def mainHill(self, plain_text):

        # Convert the plain text to uppercase
        plain_text = plain_text.upper()

        # Remove any spaces from the plain text
        plain_text = plain_text.replace(" ", "")

        # Pad the plain text if its length is not a multiple of the key matrix size
        if len(plain_text) % len(self.key) != 0:
            padding_length = len(self.key) - (len(plain_text) % len(self.key))
            plain_text += 'X' * padding_length

        # Initialize the cipher text
        cipher_text = ''

        # Encrypt the plain text
        for i in range(0, len(plain_text), len(self.key)):
            # Get the current block of the plain text
            block = plain_text[i:i + len(self.key)]

            # Convert the block to a column vector of numbers
            block_vector = np.array([ord(ch) - ord('A') for ch in block])

            # Multiply the key matrix with the block vector
            encrypted_vector = np.dot(self.key, block_vector) % 26

            # Convert the encrypted vector back to a string
            encrypted_block = ''.join([chr(num + ord('A')) for num in encrypted_vector])

            # Append the encrypted block to the cipher text
            cipher_text += encrypted_block

        return cipher_text

    def encrypt(self, plain_text):
        cipher_text = self.mainHill(plain_text)
        decrypt_key = np.array(self.matrix_inverse_mod())
        print(f'cipher {cipher_text}')
        print(f'key {decrypt_key}')
        return cipher_text, decrypt_key

    def decrypt(self, plain_text):
        cipher_text = self.mainHill(plain_text)
        return cipher_text
