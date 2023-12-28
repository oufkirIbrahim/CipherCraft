import random
import string


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
        def transposition_key(min_r=0, max_r=10):
            """
            Generate a random Transposition cipher key
            :return: int
            """
            return random.randint(min_r, max_r)

        @staticmethod
        def multiplicative_key():
            """
            Generate a random Multiplicative cipher key
            :return:
            """

            # MUST BE COPRIME WITH 26
            return random.choice([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])

        @staticmethod
        def hill_key(m=2, n=5):
            """
            Generate a random Hill cipher key
            :param m:
            :param n:
            :return: key_matrix
            """
            matrix_size = random.randint(m, n)
            key_matrix = [[random.randint(1, 26) for _ in range(matrix_size)] for _ in range(matrix_size)]
            return key_matrix

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
            return KeyGenerator.generate_random_key(32)


