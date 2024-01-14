import CipherCraft.utils.enums.preference as pr
from CipherCraft.classic import caesar, hill,  affine, multiplicative, permutation, transposition, Vigenere
from CipherCraft.modern import rc4, des, aes, rsa
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
        return

    def _caesar(self, key):
        return self.validator.digits_only(key)

    def _hill(self, key):
        return

    def _multiplicative(self, key):
        return

    def _permutation(self, key):
        return

    def _transposition(self, key):
        return

    def _vigenere(self, key):
        return

    def _aes(self, key):
        return

    def _des(self, key):
        return

    def _rc4(self, key):
        return

    def _rsa(self, key):
        return
