from CipherCraft.classic.caesar import Caesar


def test_caesar_cipher_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    caesar_cipher = Caesar(12)
    cipher_text1 = caesar_cipher.encrypt('Life Is Always Runnig Out')
    cipher_text2 = caesar_cipher.encrypt('Lets Be AWESOME')

    assert cipher_text1 == 'Xurq Ue Mximke Dgzzus Agf'
    assert cipher_text2 == 'Xqfe Nq MIQEAYQ'


def test_caesar_cipher_decryption():

    # TEST THE DECRYPTION BY THE SAME KEY
    caesar_cipher = Caesar(5)
    plain_text_1 = caesar_cipher.decrypt('kjfw Ymj Zsptbs')
    plain_text_2 = caesar_cipher.decrypt('Gj Gjyyjw ymfs jajw')

    assert plain_text_1 == 'fear The Unkown'
    assert plain_text_2 == 'Be Better than ever'

