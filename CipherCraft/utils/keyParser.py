from CipherCraft.utils.Generators.errorLogger import ErrorLogger


class KeyParser:

    def __init__(self):
        self.error_log = ErrorLogger()

    def parse_string(self, str_key):
        """Function To Parse String"""
        try:
            return str(str_key)
        except Exception as e:
            self.error_log.error_log(e)
            return None

    def parse_affine(self, str_key):
        """Function To Parse Affine Cipher Key"""
        try:
            return list([int(i) for i in str_key.split(',')])
        except Exception as e:
            self.error_log.error_log(e)
            return None

    def parse_caesar(self, str_key):
        """Function To Parse Caesar Cipher Key"""
        try:
            return int(str_key)
        except Exception as e:
            self.error_log.error_log(e)
            return None

    def parse_hill(self, str_key):
        """Function To Parse Hill Cipher Key"""
        try:
            return [[int(j) for j in i.split(',')] for i in str_key.split(':')]
        except Exception as e:
            self.error_log.error_log(e)
            return None

    def parse_multiplicative(self, str_key):
        """Function To Parse Multiplicative Cipher Key"""
        try:
            return int(str_key)
        except Exception as e:
            self.error_log.error_log(e)
            return None

    def parse_permutation(self, str_key):
        """Function To Parse Permutation Cipher Key"""
        return self.parse_string(str_key)

    def parse_transposition(self, str_key):
        """Function To Parse Transposition Cipher Key"""
        try:
            return list([int(i) for i in str_key.split(',')])
        except Exception as e:
            self.error_log.error_log(e)
            return None

    def parse_vigenere(self, str_key):
        """Function To Parse Vigenere Cipher Key"""
        return self.parse_string(str_key)

    def parse_des(self, str_key):
        """Function To Parse DES Cipher Key"""
        return self.parse_string(str_key)

    def parse_aes(self, str_key):
        """Function To Parse AES Cipher Key"""
        return self.parse_string(str_key)

    def parse_rc4(self, str_key):
        """Function To Parse RC4 Cipher Key"""
        return self.parse_string(str_key)

    def parse_rsa(self, str_key):
        """Function To Parse RSA Cipher Key"""
        try:
            return tuple([int(i) for i in str_key.split(',')])
        except Exception as e:
            return self.parse_string(str_key)
