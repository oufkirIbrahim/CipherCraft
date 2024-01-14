from CipherCraft.classic.hill import HillCipher


def test_hill_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    hill_cipher = HillCipher([[9, 4], [5, 7]])
    cipher_text1, key1 = hill_cipher.encrypt('Je Vous Aime')
    cipher_text2, key2 = hill_cipher.encrypt('Hello world')
    assert cipher_text1 == 'TvLvssGeuk'.upper()
    assert cipher_text2 == 'Blncgqmhhy'.upper()


def test_hill_decryption():

    # TEST THE DECRYPTION BY THE SAME KEY
    hill_cipher = HillCipher([[5, 12], [15, 25]])
    plain_text_1 = hill_cipher.decrypt('TvLvssGeuk'.upper())
    plain_text_2 = hill_cipher.decrypt('Blncgqmhhy'.upper())

    assert plain_text_1 == 'JEVOUSAIME'
    assert plain_text_2 == 'HELLOWORLD'

