from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from unittest.mock import patch


def test_affine_key():
    # CONTROLLING THE BEHAVIOR OF THE MOCKED FUNCTION
    with patch("CipherCraft.utils.Generators.keyGenerator.random.choice", return_value=3), \
            patch("CipherCraft.utils.Generators.keyGenerator.random.randint", return_value=0):
        a, b = KeyGenerator().Classic.affine_key()
        assert a == 3
        assert b == 0
