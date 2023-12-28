from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from unittest.mock import patch


def test_multiplicative_key():
    # CONTROLLING THE BEHAVIOR OF THE MOCKED FUNCTION
    with patch("CipherCraft.utils.Generators.keyGenerator.random.choice", return_value=3):
        key = KeyGenerator().Classic.multiplicative_key()
        assert key == 3
