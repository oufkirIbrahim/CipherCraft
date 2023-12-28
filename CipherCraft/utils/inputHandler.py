import re


class InputHandler:
    def __init__(self):
        pass

    @staticmethod
    def input_validation(user_input, regex) -> bool:
        """
        This Function Perform Input Validation Based On The Provided Regex Pattern
        :param regex:
        :param user_input:
        :return: bool
        """
        pattern = re.compile(regex)
        return bool(pattern.match(user_input))

    @staticmethod
    def letters_only(user_input) -> bool:
        """
        This Function Perform Input Validation for letters Only
        :param user_input:
        :return: bool
        """

        # LETTERS ONLY PATTERN
        regex = r'^[a-zA-Z]+$'
        return InputHandler.input_validation(user_input, regex)

    @staticmethod
    def digits_only(user_input) -> bool:
        """
        This Function Perform Input Validation For Digits Only
        :param user_input:
        :return: bool
        """

        # DIGITS ONLY PATTERN
        regex = r'^[0-9]+$'
        return InputHandler.input_validation(user_input, regex)
