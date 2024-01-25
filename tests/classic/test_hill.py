from CipherCraft.classic.hill import HillCipher


def test_hill_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    hill_cipher = HillCipher([[9, 4], [5, 7]])
    cipher_text1 = hill_cipher.encrypt('Je Vous Aime')
    cipher_text2 = hill_cipher.encrypt('Hello world')
    assert cipher_text1 == 'TVLVSSGEUK'
    assert cipher_text2 == 'BLNCGQMHHY'


def test_hill_decryption():

    # TEST THE DECRYPTION BY THE SAME KEY
    hill_cipher = HillCipher([[5, 12], [15, 25]])
    plain_text_1 = hill_cipher.decrypt('TVLVSSGEUK')
    plain_text_2 = hill_cipher.decrypt('BLNCGQMHHY')

    assert plain_text_1 == 'JEVOUSAIME'
    assert plain_text_2 == 'HELLOWORLD'

