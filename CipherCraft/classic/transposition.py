import numpy as np


class TranspositionCipher:
    def __init__(self, key):
        # Initialize the TranspositionCipher with a permutation key
        self.key = key
        self.keyLength = len(key)

    def mainTransposition(self, text):
        # Encrypt or decrypt the text using transposition cipher
        processed_text = ""
        text_ns = text.replace(' ', '')

        # Initialize a block for permutation
        permuted_block = ["x"] * self.keyLength

        for i in range(0, len(text_ns), self.keyLength):
            block = text_ns[i:i + self.keyLength]
            if len(block) < self.keyLength:
                block = block + '🔠' * (self.keyLength - len(block))

            # Permute the block based on the key
            for j in range(0, self.keyLength):
                permuted_block[j] = block[self.key[j]-1]

            # Add the permuted block to the processed text
            processed_text += "".join(permuted_block)

        for i, char in enumerate(text):
            if char == ' ':
                # Insert spaces back at their original positions
                processed_text = processed_text[:i] + ' ' + processed_text[i:]

        return processed_text

    def encrypt(self, text):
        # Encrypt the text and return the ciphertext and decryption key
        ciphertext = self.mainTransposition(text)
        decryptKey = np.argsort(self.key) + 1

        return ciphertext

    def decrypt(self, ciphertext):
        # Decrypt the ciphertext
        return self.mainTransposition(ciphertext)
