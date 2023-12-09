from enums import Algorithm,Mode
from caesar import Caesar

class CryptoHandlerFactory:
    @staticmethod
    def create_handler(type):
        if(type == Mode.CLASSIC):
            return ClassicCryptoHandler()
        elif(type == Mode.MODERN):
            return 0
        else:
            raise ValueError(f'Unsupported encryption type: {type}')

class ClassicCryptoHandler:
    def encrypt(self,data,algo):
        if(algo == Algorithm.CAESAR):
            c = Caesar()
            c.encrypt(data)
        else:
            print("other")
    def decrypt(self,data,algo):
        if(algo == Algorithm.CAESAR):
            c = Caesar()
            c.decrypt(data)
        else:
            print("other")

