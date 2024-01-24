import CipherCraft.utils.enums.preference as pr
from CipherCraft.utils.inputHandler import InputHandler


class KeyValidator:
    def __init__(self):
        self.validator = InputHandler()
        self.mappings = {
            pr.Actions.CLASSIC.__name__(): {
                pr.ClassicAlgorithms.AFFINE.__name__(): self._affine,
                pr.ClassicAlgorithms.CAESAR.__name__(): self._caesar,
                pr.ClassicAlgorithms.HILL.__name__(): self._hill,
                pr.ClassicAlgorithms.MULTIPLICATIVE.__name__(): self._multiplicative,
                pr.ClassicAlgorithms.PERMUTATION.__name__(): self._permutation,
                pr.ClassicAlgorithms.TRANSPOSITION.__name__(): self._transposition,
                pr.ClassicAlgorithms.VIGENERE.__name__(): self._vigenere,
            },
            pr.Actions.MODERN.__name__(): {
                pr.ModernAlgorithms.AES.__name__(): self._aes,
                pr.ModernAlgorithms.DES.__name__(): self._des,
                pr.ModernAlgorithms.RC4.__name__(): self._rc4,
                pr.ModernAlgorithms.RSA.__name__(): self._rsa,
            }
        }

    def validate(self, era, algorithm, key):
        return self.mappings[era][algorithm](key)

    def _affine(self, key):
        a, b = key
        return self.validator.digits_only(str(a)) and self.validator.is_invertible(a) and self.validator.is_valid_integer(str(b))

    def _caesar(self, key):
        return self.validator.digits_only(key) and int(key) < 26

    def _hill(self, key):
        return self.validator.is_valid_hill_key(key)

    def _multiplicative(self, key):
        return self.validator.digits_only(key) and self.validator.is_invertible(key)

    def _permutation(self, key):
        return self.validator.has_duplicates(key) & self.validator.has_all_alphabet_characters(key)

    def _transposition(self, key):
        return set(key) == set(range(1, len(key)+1))

    def _vigenere(self, key):
        return self.validator.letters_only(key)

    def _aes(self, key):
        return self.validator.is_hex_string(key) and len(key) == 32

    def _des(self, key):
        return self.validator.is_hex_string(key) and len(key) == 16

    def _rc4(self, key):
        return self.validator.validate_rc4_key(key)

    def _rsa(self, key):
        if isinstance(key, tuple):
            return self.validator.validate_rsa_tuple(key)
        else:
            return self.validator.validate_pem_data(key) or self.validator.is_base64_encoded(key)