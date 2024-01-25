from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from CipherCraft.utils.keyValidator import KeyValidator
import CipherCraft.utils.enums.preference as pr

validator = KeyValidator()
generator = KeyGenerator()


def test_rsa_key():
    key = generator.Modern.rsa_key(bits=1024, test=True)
    assert validator.validate(pr.Actions.MODERN.__name__(),
                              pr.ModernAlgorithms.RSA.__name__(),
                              key)
