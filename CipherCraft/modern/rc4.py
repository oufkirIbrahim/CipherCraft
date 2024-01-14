class Rc4Cipher:
    def __init__(self, key):
        self.key = key
        # Initialize S using the key schedule
        self.S = self._key_schedule(list(range(256)))

    def _key_schedule(self, lst):
        # Internal method to perform key scheduling
        key = [ord(c) for c in self.key]
        j = 0
        S = lst  # Copy the initial permutation from the input list
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]  # Swap elements based on the key and current permutation
        return S

    def _generate_keystream(self):
        # Internal method to generate the keystream
        i = j = 0
        S = list(self.S)  # Copy the permutation to avoid modifying the original
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # Update the permutation
            yield S[(S[i] + S[j]) % 256]  # Generate the keystream value

    def encrypt(self, plaintext):
        # Encryption method using RC4
        keystream = self._generate_keystream()
        encrypted_text = []
        for char in plaintext:
            key_byte = next(keystream)
            encrypted_char = ord(char) ^ key_byte
            encrypted_text.append(encrypted_char)

        # Convert the encrypted bytes to hexadecimal representation
        return bytes(encrypted_text).hex().upper()

    def decrypt(self, ciphertext):
        # Decryption method using RC4
        keystream = self._generate_keystream()
        decrypted_text = []
        for i in range(0, len(ciphertext), 2):
            hex_pair = ciphertext[i:i+2]
            key_byte = next(keystream)
            decrypted_char = int(hex_pair, 16) ^ key_byte
            decrypted_text.append(decrypted_char)

        # Convert the decrypted bytes to a string using utf-8 encoding
        return bytes(decrypted_text).decode('utf-8')

# Example usage:
key = "not-so-random-key"
plaintext = "RC4 for Rivest Cipher 4 is a symmetric and fast cipher algorithm"

rc4_cipher = Rc4Cipher(key)

encrypted_text = rc4_cipher.encrypt(plaintext)
decrypted_text = rc4_cipher.decrypt(encrypted_text)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
