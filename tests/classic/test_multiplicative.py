from CipherCraft.classic.multiplicative import MultiplicativeCipher


def test_multiplicative_cipher_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    multiplicative_cipher = MultiplicativeCipher(7)
    cipher_text1 = multiplicative_cipher.encrypt('Home Sweet Home')
    cipher_text2 = multiplicative_cipher.encrypt('have A better Mindset. Dont Narrow Your Self')

    assert cipher_text1 == 'Xugc Wyccd Xugc'
    assert cipher_text2 == 'xarc A hcddcp Genvwcd. Vund Nappuy Mukp Wczj'


def test_multiplicative_cipher_decryption():

    # TEST THE DECRYPTION BY THE SAME KEY
    multiplicative_cipher = MultiplicativeCipher(7)
    plain_text_1 = multiplicative_cipher.decrypt('Azyamw Aqaenwd Gc')
    plain_text_2 = multiplicative_cipher.decrypt('Yxcpc dxcpc ew Yadcp Dxcpc ew Zejc')

    assert plain_text_1 == 'Always Against Me'
    assert plain_text_2 == 'Where there is Water There is Life'

