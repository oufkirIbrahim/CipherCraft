from enums import Algorithm,Mode
from caesar import Caesar
from multiplicative import MultiplicativeCipher
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

        key = int(input("Enter the key (an integer): "))
        if(algo == Algorithm.CAESAR):
            c = Caesar(key)
            c.encrypt(data) 
        elif(algo == Algorithm.MULTIPL):
            c = MultiplicativeCipher(key)
            c.encrypt(data)
        else:
            print("other")
    def decrypt(self,data,algo):

        key = int(input("Enter the key (an integer): "))
        if(algo == Algorithm.CAESAR):
            c = Caesar(key)
            c.decrypt(data)
        elif(algo == Algorithm.MULTIPL):
            c = MultiplicativeCipher(key)
            c.decrypt(data)
        else:
            print("other")

