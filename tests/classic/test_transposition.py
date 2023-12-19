from CipherCraft.classic.transposition import TranspositionCipher
import numpy as np

def test_transposition_cipher_encryption():

    key = [3, 5, 1, 6, 4,2]
    transposition_copher = TranspositionCipher(key)

    cipher_text,arr = transposition_copher.encrypt("ALI VA A L ECOLE")

    assert cipher_text == "IAA AV L C LLEOE"



def test_transposition_cipher_decryption():
    key = [3, 6, 1, 5, 2, 4]
    transposition_copher = TranspositionCipher(key)

    plain_text1 = transposition_copher.decrypt("IAA AV L C LLEOE")

    assert plain_text1 == "ALI VA A L ECOLE"