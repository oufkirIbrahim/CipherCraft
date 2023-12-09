from enums import Algorithm,Mode
from caesar import Caesar
from multiplicative import MultiplicativeCipher
from affine import AffineCipher
class CryptoHandlerFactory:
    @staticmethod
    def create_handler(mode):
        if(mode == Mode.CLASSIC):
            return ClassicCryptoHandler()
        elif(mode == Mode.MODERN):
            return 0
        else:
            raise ValueError(f'Invalid mode {mode}. Please choose either "classic" or "modern".')

class ClassicCryptoHandler:
    def encrypt(self,data,algo):

        

        if(algo == Algorithm.CAESAR):
            key = int(input("Enter the key (an integer): "))
            c = Caesar(key)
            c.encrypt(data) 
        elif(algo == Algorithm.MULTIPL):
            key = int(input("Enter the key (an integer): "))
            c = MultiplicativeCipher(key)
            c.encrypt(data)
        elif(algo == Algorithm.AFFINE):
            a = int(input("Enter the value for 'a' (multiplicative key): "))
            b = int(input("Enter the value for 'b' (additive key): "))
            c = AffineCipher(a,b)
            c.encrypt(data)
        else:
            print("other")
    def decrypt(self,data,algo):

        if(algo == Algorithm.CAESAR):
            key = int(input("Enter the key (an integer): "))
            c = Caesar(key)
            c.decrypt(data)
        elif(algo == Algorithm.MULTIPL):
            key = int(input("Enter the key (an integer): "))
            c = MultiplicativeCipher(key)
            c.decrypt(data)
        elif(algo == Algorithm.AFFINE):
            a = int(input("Enter the value for 'a' (multiplicative key): "))
            b = int(input("Enter the value for 'b' (additive key): "))
            c = AffineCipher(a,b)
            c.decrypt(data)
        else:
            print("other")

