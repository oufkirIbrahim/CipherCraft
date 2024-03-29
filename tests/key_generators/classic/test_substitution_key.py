from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from CipherCraft.utils.keyValidator import KeyValidator
import CipherCraft.utils.enums.preference as pr

validator = KeyValidator()
generator = KeyGenerator()


def test_permutation_key():
    key = generator.Classic.permutation_key()
    assert validator.validate(pr.Actions.CLASSIC.__name__(),
                              pr.ClassicAlgorithms.PERMUTATION.__name__(),
                              key)
