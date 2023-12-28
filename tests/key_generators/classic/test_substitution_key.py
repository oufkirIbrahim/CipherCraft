from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from unittest.mock import patch


def test_substitution_key():
    # CONTROLLING THE BEHAVIOR OF THE MOCKED FUNCTION
    with patch("CipherCraft.utils.Generators.keyGenerator.random.choice", return_value='A'):
        key = KeyGenerator().Classic.substitution_key()
        assert isinstance(key, dict)
        assert 'A' in key.values()
