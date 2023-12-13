class Vigenere:

    def __init__(self, key):
        """

        :param key:
        """
        self.key = key

    def shift_text(self, plaintext, operation='encrypt'):

        """

        :param plaintext:
        :param operation:
        :return: shifted_text
        """
        # INITIALIZING THE VARS
        encrypted_text = ""
        key_index = 0
        key_length = len(self.key)
        key = self.key

        # LOOPING THE PLAINTEXT
        for char in plaintext:

            # CHECK IF THE CHAR IS ALPHANUMERIC
            if char.isalpha():

                # GETTING THE SHIFT VALUE FROM THE CURRENT KEY INDEX
                shift = ord(key[key_index].upper()) - ord('A')

                if operation == 'encrypt':
                    
                    # ENCRYPT THE CURRENT CHAR BASED ON THE CASE
                    if char.isupper():
                        encrypted_text += self.shift_char(char, 'A', shift)
                    else:
                        encrypted_text += self.shift_char(char, 'a', shift)
                
                elif operation == 'decrypt':

                    # DECRYPT THE CURRENT CHAR BASED ON THE CASE
                    if char.isupper():
                        encrypted_text += self.shift_char(char, 'A', shift, '-')
                    else:
                        encrypted_text += self.shift_char(char, 'a', shift, '-')
                else:
                    # UNSPECIFIED OPERATION: DO NOTHING
                    encrypted_text += char
                    
                # SHIFTING THE KEY BUFFER
                key_index = (key_index + 1) % key_length
            else:
                # NON ALPHABETIC CHAR DETECTED: DO NOTHING
                encrypted_text += char
        
        # RETURN THE ENCRYPTED TEXT
        return encrypted_text

    def encrypt(self, plaintext):
        """
        
        :param plaintext: 
        :return: encrypted_text
        """
        return self.shift_text(plaintext)

    def decrypt(self, ciphertext):
        """

        :param ciphertext: 
        :return: plaintext
        """
        return self.shift_text(ciphertext, "decrypt")

    @staticmethod
    def shift_char(char, base_char, shift, operator='+'):

        """
        :param char:
        :param base_char:
        :param shift:
        :param operator:
        :return: shifted_char
        """

        # THE NUMERICAL VALUE OF CHAR
        char_code = ord(char) - ord(base_char)

        # APPLYING THE SHIFTING ON THE CURRENT CHAR
        if operator == "-":

            # BACKWARD SHIFT
            return chr((char_code - shift) % 26 + ord(base_char))
        elif operator == '+':

            # FORWARD SHIFT
            return chr((char_code + shift) % 26 + ord(base_char))
        else:

            # UNSUPPORTED OPERATOR
            return char





