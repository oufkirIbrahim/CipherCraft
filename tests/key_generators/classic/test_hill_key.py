from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from CipherCraft.utils.keyValidator import KeyValidator
import CipherCraft.utils.enums.preference as pr

validator = KeyValidator()
generator = KeyGenerator()


def test_hill_key():
    key = generator.Classic.hill_key()
    assert validator.validate(pr.Actions.CLASSIC.__name__(),
                              pr.ClassicAlgorithms.HILL.__name__(),
                              key)
