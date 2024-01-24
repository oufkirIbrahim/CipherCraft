from CipherCraft.modern.aes import AesCipher


def test_rc4_cipher_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    aes_cipher = AesCipher('2b7e151628aed2a6abf7158809cf4f3c')
    cipher_text = aes_cipher.encrypt("3243f6a8885a308d313198a2e0370734")
    cipher_text_2 = aes_cipher.encrypt("72d5135800aed2a6abf7158809cf4f3c")
    assert cipher_text == '3925841d02dc09fbdc118597196a0b32'

    assert cipher_text_2 == '26a139459a1f7635bb1ae03c02656657'

def test_rc4_cipher_decryption():
    aes_cipher = AesCipher('2b7e151628aed2a6abf7158809cf4f3c')
    plain_text = aes_cipher.decrypt('3925841d02dc09fbdc118597196a0b32')
    plain_text_2 = aes_cipher.decrypt("26a139459a1f7635bb1ae03c02656657")
    assert plain_text == '3243f6a8885a308d313198a2e0370734'

    assert plain_text_2 == '72d5135800aed2a6abf7158809cf4f3c'
