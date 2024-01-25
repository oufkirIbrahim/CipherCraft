from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from CipherCraft.utils.keyValidator import KeyValidator
import CipherCraft.utils.enums.preference as pr

validator = KeyValidator()
generator = KeyGenerator()


def test_des_key():
    key = generator.Modern.des_key()
    assert validator.validate(pr.Actions.MODERN.__name__(),
                              pr.ModernAlgorithms.DES.__name__(),
                              key)
