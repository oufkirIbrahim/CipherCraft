from CipherCraft.classic.Vigenere import Vigenere


def test_vigenere_cipher_encryption():

    # TEST THE ENCRYPTION BY THE SAME KEY
    vigenere_cipher = Vigenere('key')
    cipher_text1 = vigenere_cipher.encrypt('This Is Test One')
    cipher_text2 = vigenere_cipher.encrypt('13-12-2023 It May Takes Time, But It Will HAPPEN No Matter What!')

    assert cipher_text1 == 'Dlgc Mq Diqd Slo'
    assert cipher_text2 == '13-12-2023 Sx Kkc Rkocc Xgwi, Zex Gd Agvp FKTNOR Ly Qydxcb Afkx!'
    return


def test_vigenere_cipher_decryption():
    vigenere_cipher = Vigenere('OnlyThisOne')
    plain_text_1 = vigenere_cipher.decrypt('Hvxc Bz Xsgfmbt , Ymm Acjbvru Olad')
    plain_text_2 = vigenere_cipher.decrypt('2023 CAP UTF, Wfs Plcvnc . Xpbzse Awa Zp Evaw')

    assert plain_text_1 == 'Time Is Passing , Not Turning Back'
    assert plain_text_2 == '2023 ONE WAY, One Choice . Either Win Or Lose'

