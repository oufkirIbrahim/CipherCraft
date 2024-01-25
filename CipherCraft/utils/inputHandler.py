import binascii
import re
import numpy as np
import base64


class InputHandler:
    def __init__(self):
        pass

    @staticmethod
    def input_validation(user_input, regex) -> bool:
        """
        Perform input validation based on the provided regex pattern.
        :param regex: Regular expression pattern.
        :param user_input: User input string.
        :return: True if the input matches the pattern, False otherwise.
        """
        pattern = re.compile(regex)
        return bool(pattern.match(user_input))

    @staticmethod
    def letters_only(user_input) -> bool:
        """
        Perform input validation for letters only.
        :param user_input: User input string.
        :return: True if the input contains only letters, False otherwise.
        """

        # LETTERS ONLY PATTERN
        regex = r'^[a-zA-Z]+$'
        return InputHandler.input_validation(user_input, regex)

    @staticmethod
    def digits_only(user_input) -> bool:
        """
        Perform input validation for digits only.
        :param user_input: User input string.
        :return: True if the input contains only digits, False otherwise.
        """

        # DIGITS ONLY PATTERN
        regex = r'^[0-9]+$'
        return InputHandler.input_validation(str(user_input), regex)

    @staticmethod
    def is_valid_integer(user_input) -> bool:
        """
        Perform input validation for a valid integer.
        :param user_input: User input string.
        :return: True if the input is a valid integer, False otherwise.
        """
        regex = r'^-?\d+$'
        return InputHandler.input_validation(user_input, regex)

    @staticmethod
    def is_invertible(a) -> bool:
        """
        Check if a number is invertible.
        :param a: Integer to check for invertibility.
        :return: True if 'a' is invertible, False otherwise.
        """
        invertibles = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        return int(a) in invertibles

    @staticmethod
    def has_all_alphabet_characters(user_input) -> bool:
        """
        Check if the input contains all alphabet characters.
        :param user_input: User input string.
        :return: True if the input contains all alphabet characters, False otherwise.
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for c in user_input:
            if c not in alphabet:
                return False
        return True

    @staticmethod
    def has_duplicates(user_input) -> bool:
        """
        Check if the input contains duplicate characters.
        :param user_input: User input string.
        :return: True if the input contains duplicate characters, False otherwise.
        """
        return len(user_input) == len(set(user_input))

    @staticmethod
    def is_hex_string(user_input) -> bool:
        """
        Check if the input is a valid hexadecimal string.
        :param user_input: User input string.
        :return: True if the input is a valid hexadecimal string, False otherwise.
        """
        regex = r'^[0-9a-fA-F]+$'
        return InputHandler.input_validation(user_input, regex)

    @staticmethod
    def validate_rc4_key(user_input) -> bool:
        """
        Validate the input for RC4 key.
        :param user_input: User input string.
        :return: True if the input is a valid RC4 key, False otherwise.
        """
        regex = r'^[ -~]+$'
        return InputHandler.input_validation(user_input, regex)

    @staticmethod
    def mod_inverse(a, m):
        """
        Extended Euclidean Algorithm to find the modular inverse.
        :param a: Integer.
        :param m: Modulus.
        :return: Modular inverse of 'a' modulo 'm'.
        """
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    @staticmethod
    def is_square(matrix):
        """
        Check if the matrix is square.
        :param matrix: 2D matrix.
        :return: True if the matrix is square, False otherwise.
        """
        return all(len(row) == len(matrix) for row in matrix)

    @staticmethod
    def is_valid_hill_key(key_matrix):
        """
        Check if the key matrix is a valid Hill cipher key.
        :param key_matrix: 2D matrix.
        :return: True if the key matrix is a valid Hill cipher key, False otherwise.
        """

        for elm in key_matrix:
            if (len(elm) != len(key_matrix)):
                return False

        key_matrix = np.array(key_matrix)

        # Check if the key matrix is square
        if not InputHandler.is_square(key_matrix):
            return False

        # Calculate determinant of the key matrix
        det = int(round(np.linalg.det(key_matrix))) % 26

        # Check if the determinant is non-zero
        if det == 0:
            return False

        try:
            # Check if the determinant has a modular multiplicative inverse in Z_26
            return InputHandler.mod_inverse(det, 26) is not None
        except ZeroDivisionError:
            return False

    @staticmethod
    def validate_rsa_list(key):
        a, b = key
        return isinstance(key, list) and a > b > 0

    @staticmethod
    def is_base64_encoded(text):
        try:
            # Attempt to decode the text
            decoded_bytes = base64.b64decode(text)

            # If decoding is successful, check if the result can be decoded as UTF-8
            decoded_text = decoded_bytes.decode('utf-8')

            # If decoding as UTF-8 is successful, the input is likely Base64-encoded
            return True
        except (binascii.Error, UnicodeDecodeError):
            # If decoding fails, it's not Base64-encoded

            return False

    @staticmethod
    def validate_start_marker(marker):
        regex = r'^-{5}BEGIN\s(PUBLIC|PRIVATE)\sKEY-{5}'
        return InputHandler.input_validation(marker, regex)

    @staticmethod
    def validate_end_marker(marker):
        regex = r'-{5}END\s(PUBLIC|PRIVATE)\sKEY-{5}'
        return InputHandler.input_validation(marker, regex)

    @staticmethod
    def validate_pem_data(text_key):
        array_key = text_key.strip().split("\n")
        start_marker = array_key[0]
        end_marker = array_key[-1]
        key = ''.join(array_key[1:-1])
        return (InputHandler.validate_start_marker(start_marker) and
                InputHandler.validate_end_marker(end_marker) and
                InputHandler.is_base64_encoded(key))
