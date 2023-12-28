from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from unittest.mock import patch


def test_caesar_key():

    # CONTROLLING THE BEHAVIOR OF THE MOCKED FUNCTION
    with patch("CipherCraft.utils.Generators.keyGenerator.random.choices", return_value='A'):
        key = KeyGenerator().Classic.caesar_key()
        assert key == 'A'

