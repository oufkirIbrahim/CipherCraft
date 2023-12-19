from CipherCraft.classic.permutation import PermutationCipher


def test_permutation_cipher_encryption():

    key = "cghwzqtnmlsxvryeofdjikupba"
    permutation_cipher = PermutationCipher(key)

    cipher_text1 = permutation_cipher.encrypt('i want to meet you')
    cipher_text2 = permutation_cipher.encrypt(
        'matrix has an inverse if and only if its only entry has a multiplicative inverse in the ring it is taken from'
    )

    assert cipher_text1 == "m ucrj jy vzzj byi"
    assert cipher_text2 == "vcjfmp ncd cr mrkzfdz mq crw yrxb mq mjd yrxb zrjfb ncd c vixjmexmhcjmkz mrkzfdz mr jnz fmrt mj md jcszr qfyv"


def test_permutation_cipher_decryption():

    key = "cghwzqtnmlsxvryeofdjikupba"
    permutation_cipher = PermutationCipher(key)

    plain_text1 = permutation_cipher.decrypt("m ucrj jy vzzj byi")
    plain_text2 = permutation_cipher.decrypt("vcjfmp ncd cr mrkzfdz mq crw yrxb mq mjd yrxb zrjfb ncd c vixjmexmhcjmkz mrkzfdz mr jnz fmrt mj md jcszr qfyv")

    assert plain_text1 == "i want to meet you"
    assert plain_text2 == "matrix has an inverse if and only if its only entry has a multiplicative inverse in the ring it is taken from"
    