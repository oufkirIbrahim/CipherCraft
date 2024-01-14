from CipherCraft.modern.rc4 import Rc4Cipher


def test_rc4_cipher_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    rc4_cipher = Rc4Cipher('not-so-random-key')
    cipher_text1 = rc4_cipher.encrypt('Hello RC4!')
    cipher_text2 = rc4_cipher.encrypt('RC4 for Rivest Cipher 4 is a symmetric and fast cipher algorithm')

    assert cipher_text1 == '2275ED71B099BD8682B7'
    assert cipher_text2 == '3853B53DB9D69DE5E4FFEB99BBF92AAD299B0D4E78CBA2F68DEF134EF130D6700DD0EF99AFB219EB63D83FB1710189CDEC8FB099BF6FBCE3E9859619995720CF'
    return


def test_rc4_cipher_decryption():
    rc4_cipher = Rc4Cipher('not-so-random-key')
    plain_text_1 = rc4_cipher.decrypt('2275ED71B099BD8682B7')
    plain_text_2 = rc4_cipher.decrypt('3853B53DB9D69DE5E4FFEB99BBF92AAD299B0D4E78CBA2F68DEF134EF130D6700DD0EF99AFB219EB63D83FB1710189CDEC8FB099BF6FBCE3E9859619995720CF')

    assert plain_text_1 == 'Hello RC4!'
    assert plain_text_2 == 'RC4 for Rivest Cipher 4 is a symmetric and fast cipher algorithm'

