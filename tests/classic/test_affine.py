from CipherCraft.classic.affine import AffineCipher


def test_affine_cipher_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    affine_cipher = AffineCipher(5, 8)
    cipher_text1 = affine_cipher.encrypt('The quick brown fox jumps over 13 lazy dogs.')
    cipher_text2 = affine_cipher.encrypt('One Day It will End . But Never Mind It Lasts For Ever!')

    assert cipher_text1 == 'Zrc kewsg npaov hat beqfu ajcp 13 lidy xamu.'
    assert cipher_text2 == 'Avc Xiy Wz owll Cvx . Nez Vcjcp Qwvx Wz Liuzu Hap Cjcp!'


def test_affine_cipher_decryption():

    # TEST THE DECRYPTION BY THE SAME KEY
    affine_cipher = AffineCipher(3, 16)
    plain_text_1 = affine_cipher.decrypt('Gdwc Ov Lqjjcds , Ov Xqsvs')
    plain_text_2 = affine_cipher.decrypt('2023 Lqs Cdzcz , Q dce Svqpv Qeqovs Ys , Eosl Ec Sywwccz')

    assert plain_text_1 == 'Once It Happens , It Lasts'
    assert plain_text_2 == '2023 Has Ended , A new Start Awaits Us , Wish We Succeed'

