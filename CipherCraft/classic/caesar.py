
class Caesar:
    def __init__(self, key):
        if type(key) == str and key.isalpha():
            self.key = ord(key.upper()) - ord('A')
        else:
            self.key = int(key)

    def encrypt(self, data):
        result = ""

        # traverse text
        for i in range(len(data)):
            char = data[i]
    
            if char.isalpha():
                # Encrypt uppercase characters
                if char.isupper():
                    result += chr((ord(char) + self.key - 65) % 26 + 65)

                # Encrypt lowercase characters
                else:
                    result += chr((ord(char) + self.key - 97) % 26 + 97)
            else:
                result += char
        return result

    def decrypt(self, data):
        result = ""

        # traverse text
        for i in range(len(data)):
            char = data[i]
    
            if char.isalpha():

                # Encrypt uppercase characters
                if char.isupper():
                    result += chr((ord(char) - self.key - 65) % 26 + 65)

                # Encrypt lowercase characters
                else:
                    result += chr((ord(char) - self.key - 97) % 26 + 97)
            else:
                result += char

        return result

