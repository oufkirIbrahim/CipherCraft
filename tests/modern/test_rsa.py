from CipherCraft.modern.rsa import RsaCipher


def test_aes_encryption():
    # TEST THE ENCRYPTION BY THE SAME KEY
    rsa_cipher = RsaCipher.RsaExecutor([221, 35])
    cipher_text = rsa_cipher.encrypt("Be Productive, Think Out Of The Box")
    assert cipher_text == '196 186 128 215 147 15 94 26 109 194 27 118 186 99 128 50 195 27 206 74 128 209 26 194 128 209 136 128 50 195 186 128 196 15 35'


def test_aes_decryption():
    rsa_cipher = RsaCipher.RsaExecutor([221, 11])
    plain_text = rsa_cipher.decrypt('196 186 128 215 147 15 94 26 109 194 27 118 186 99 128 50 195 27 206 74 128 209 26 194 128 209 136 128 50 195 186 128 196 15 35')
    assert plain_text == 'Be Productive, Think Out Of The Box'

