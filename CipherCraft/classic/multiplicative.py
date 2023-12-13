class MultiplicativeCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()
                
                # Apply encryption formula: C = (P * key) % 26
                encrypted_char = chr(((ord(char) - 65) * self.key) % 26 + 65)
                
                # Maintain the case of the original character
                if not is_upper:
                    encrypted_char = encrypted_char.lower()
                
                ciphertext += encrypted_char
            else:
                # If the character is not an alphabet letter, leave it unchanged
                ciphertext += char
        
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        # Find the modular multiplicative inverse of the key (assuming the key and 26 are coprime)
        inverse_key = pow(self.key, -1, 26)

        for char in ciphertext:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()

                # Apply decryption formula: P = (C * inverse_key) % 26
                decrypted_char = chr(((ord(char) - 65) * inverse_key) % 26 + 65)

                # Maintain the case of the original character
                if not is_upper:
                    decrypted_char = decrypted_char.lower()

                plaintext += decrypted_char
            else:
                plaintext += char

        return plaintext
