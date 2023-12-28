from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from unittest.mock import patch


def test_vigenere_key():
    # CONTROLLING THE BEHAVIOR OF THE MOCKED FUNCTION
    with patch("CipherCraft.utils.Generators.keyGenerator.random.choices", return_value='KEY'), \
            patch("CipherCraft.utils.Generators.keyGenerator.random.randint", return_value=5):
        key = KeyGenerator().Classic.vigenere_key(min_r=1, max_r=10)
        assert key == 'KEY'

