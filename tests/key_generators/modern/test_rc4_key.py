from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from CipherCraft.utils.keyValidator import KeyValidator
import CipherCraft.utils.enums.preference as pr

validator = KeyValidator()
generator = KeyGenerator()


def test_rc4_key():
    key = generator.Modern.rc4_key()
    assert validator.validate(pr.Actions.MODERN.__name__(),
                              pr.ModernAlgorithms.RC4.__name__(),
                              key)
