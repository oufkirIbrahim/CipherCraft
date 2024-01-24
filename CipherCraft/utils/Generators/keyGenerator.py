import math
import random
import string

import numpy as np

from CipherCraft.modern.rsa import RsaCipher


class KeyGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_random_key(length):
        """
        Generates A Random key With Specific Length
        :param length:
        :return: str
        """
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    class Classic:
        def __init__(self):
            pass

        @staticmethod
        def caesar_key():
            """
            Generate a random Caesar cipher key
            :return: str
            """
            return KeyGenerator.generate_random_key(1)

        @staticmethod
        def affine_key():
            """
            Generate a random Affine cipher key
            :return: a, b
            """

            # A IS COPRIME WITH 26
            a = random.choice([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])
            b = random.randint(0, 25)
            return a, b

        @staticmethod
        def vigenere_key(min_r=0, max_r=10):
            """
            Generate a random Vigenere cipher key
            :param min_r:
            :param max_r:
            :return: str
            """
            return KeyGenerator.generate_random_key(random.randint(min_r, max_r))

        @staticmethod
        def transposition_key(key_len=5):
            """
            Generate a random Transposition cipher key
            :return: int
            """
            key = list(range(1, key_len + 1))
            random.shuffle(key)
            return key

        @staticmethod
        def multiplicative_key():
            """
            Generate a random Multiplicative cipher key
            :return:
            """

            # MUST BE COPRIME WITH 26
            return random.choice([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])

        @staticmethod
        def hill_key(min_num=2, max_num=5):
            """
            Generate a random Hill cipher key
            :param max_num:
            :param min_num:
            :return: key_matrix
            """

            def mod_inverse(a, m):
                """Calculate the modular inverse of a modulo m."""
                if m == 0:
                    return None

                m0, x0, x1 = m, 0, 1

                while a > 1:
                    q = a // m
                    m, a = a % m, m
                    x0, x1 = x1 - q * x0, x0

                    if m == 0:
                        return None

                return x1 + m0 if x1 < 0 else x1

            def generate_invertible_matrix(n):
                """Generate an invertible square matrix of size n over Zn=26."""
                while True:
                    # Generate a random matrix with values in Zn=26
                    matrix = np.random.randint(26, size=(n, n))

                    # Ensure the matrix is invertible
                    det = int(round(np.linalg.det(matrix))) % 26
                    if det != 0:
                        # Calculate the modular inverse only if the determinant is non-zero
                        mod_inv = mod_inverse(det, 26)
                        if mod_inv is not None:
                            return matrix

            matrix_size = random.randint(min_num, max_num)
            key_matrix = generate_invertible_matrix(matrix_size)
            return [list(i) for i in key_matrix]

        @staticmethod
        def permutation_key():
            key = list(string.ascii_lowercase)
            random.shuffle(key)

            return ''.join(key)

        @staticmethod
        def substitution_key():
            """
            Generate a random Substitution cipher key
            :return: dict
            """
            alphabet = list(string.ascii_uppercase)
            random.shuffle(alphabet)
            return dict(zip(string.ascii_uppercase, alphabet))

    class Modern:
        def __init__(self):
            pass

        @staticmethod
        def aes_key():
            """
            Generate a random AES key
            :return:
            """
            rand_choices = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            return ''.join(random.choices(rand_choices, k=32))

        @staticmethod
        def des_key():
            """
            Generate a random DES key
            :return:
            """
            rand_choices = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            return ''.join(random.choices(rand_choices, k=16))

        @staticmethod
        def rc4_key(min_length=16):
            """
            Generate a random RC4 key
            :return:
            """
            printable = string.digits + string.ascii_letters + string.punctuation
            key_vals = list(printable)
            return ''.join(random.choices(key_vals, k=min_length))

        @staticmethod
        def rsa_key(bits=1024):
            """
            Generate a random rsa key
            :return:
            """
            rsa = RsaCipher.RsaGenerator(bits)


