from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from unittest.mock import patch


def test_hill_key():
    # CONTROLLING THE BEHAVIOR OF THE MOCKED FUNCTION
    with patch("CipherCraft.utils.Generators.keyGenerator.random.randint", return_value=2):
        key_matrix = KeyGenerator().Classic.hill_key(m=2, n=5)
        assert len(key_matrix) == 2
        assert len(key_matrix[0]) == 2
