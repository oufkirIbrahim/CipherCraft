from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from CipherCraft.utils.keyValidator import KeyValidator
import CipherCraft.utils.enums.preference as pr

validator = KeyValidator()
generator = KeyGenerator()


def test_transposition_key():
    key = generator.Classic.transposition_key()
    assert validator.validate(pr.Actions.CLASSIC.__name__(),
                              pr.ClassicAlgorithms.TRANSPOSITION.__name__(),
                              key)
