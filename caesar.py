
class Caesar:

    @staticmethod
    def encrypt(data):
        result = ""
        k=int(input("Enter key to encrypt: "))
        # traverse text
        for i in range(len(data)):
            char = data[i]
    
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + k-65) % 26 + 65)
    
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + k - 97) % 26 + 97)
        print(result)

    @staticmethod
    def decrypt(data):
        result = ""
        k=int(input("Enter key to encrypt: "))
        # traverse text
        for i in range(len(data)):
            char = data[i]
    
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) - k-65) % 26 + 65)
    
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) - k - 97) % 26 + 97)
        print(result)

