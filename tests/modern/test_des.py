from CipherCraft.modern.des import DesCipher


def test_aes_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    des_cipher = DesCipher('1234567890abcdef')
    cipher_text = des_cipher.encrypt("abcdef1234567890")
    assert cipher_text == '86da3b518577fde4'


def test_aes_decryption():
    des_cipher = DesCipher('1234567890abcdef')
    plain_text = des_cipher.decrypt('86da3b518577fde4')
    assert plain_text == 'abcdef1234567890'

