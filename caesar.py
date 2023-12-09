
class Caesar:
    def __init__(self):
        self.key = key

    @staticmethod
    def encrypt(data):
        result = ""

        # traverse text
        for i in range(len(data)):
            char = data[i]
    
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + self.key-65) % 26 + 65)
    
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + self.key - 97) % 26 + 97)
        print(result)

    @staticmethod
    def decrypt(data):
        result = ""

        # traverse text
        for i in range(len(data)):
            char = data[i]
    
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) - self.key-65) % 26 + 65)
    
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) - self.key - 97) % 26 + 97)
        print(result)

