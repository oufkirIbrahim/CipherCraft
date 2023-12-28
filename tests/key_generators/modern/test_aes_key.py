from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from unittest.mock import patch


def test_aes_key():
    # CONTROLLING THE BEHAVIOR OF THE MOCKED FUNCTION
    with patch("CipherCraft.utils.Generators.keyGenerator.random.choice", return_value='A'):
        key = KeyGenerator().Modern.aes_key()
        assert len(key) == 32
        # assert 'A' in key
