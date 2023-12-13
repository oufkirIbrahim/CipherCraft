class AffineCipher:
    def __init__(self, a, b, m=26):
        """
        Initialize the Affine Cipher with key parameters.

        Parameters:
        - a (int): Multiplicative key.
        - b (int): Additive key.
        - m (int): Modulus (default is 26 for the English alphabet).
        """
        self.a = a
        self.b = b
        self.m = m

        # Check if 'a' and 'm' are coprime
        if self.gcd(a, m) != 1:
            raise ValueError("'a' and 'm' must be coprime for the affine cipher to work.")

    def gcd(self, a, b):
        """
        Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

        Parameters:
        - a (int): First number.
        - b (int): Second number.

        Returns:
        - int: GCD of the two numbers.
        """
        while b != 0:
            a, b = b, a % b
        return a

    def mod_inverse(self, a, m):
        """
        Calculate the modular inverse of 'a' modulo 'm' using the extended Euclidean algorithm.

        Parameters:
        - a (int): Number for which the modular inverse is calculated.
        - m (int): Modulus.

        Returns:
        - int: Modular inverse of 'a' modulo 'm'.
        """
        m0, x0, x1 = m, 0, 1

        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0

        return x1 + m0 if x1 < 0 else x1

    def encrypt(self, plaintext):
        """
        Encrypt a message using the Affine Cipher.

        Parameters:
        - plaintext (str): Message to be encrypted.

        Returns:
        - str: Encrypted message.
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()

                # Apply encryption formula: E(x) = (ax + b) mod m
                encrypted_char = chr((self.a * (ord(char) - 65) + self.b) % self.m + 65)

                # Maintain the case of the original character
                if not is_upper:
                    encrypted_char = encrypted_char.lower()

                ciphertext += encrypted_char
            else:
                # If the character is not an alphabet letter, leave it unchanged
                ciphertext += char

        return ciphertext

    def decrypt(self, ciphertext):
        """
        Decrypt an encrypted message using the Affine Cipher.

        Parameters:
        - ciphertext (str): Encrypted message.

        Returns:
        - str: Decrypted message.
        """
        plaintext = ""
        a_inv = self.mod_inverse(self.a, self.m)

        for char in ciphertext:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()

                # Apply decryption formula: D(x) = a_inv * (x - b) mod m
                decrypted_char = chr((a_inv * (ord(char) - 65 - self.b)) % self.m + 65)

                # Maintain the case of the original character
                if not is_upper:
                    decrypted_char = decrypted_char.lower()

                plaintext += decrypted_char
            else:
                # If the character is not an alphabet letter, leave it unchanged
                plaintext += char

        return plaintext

