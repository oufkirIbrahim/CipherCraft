<<<<<<< HEAD
class RsaCipher:
    pass
=======
import random
import math

class RsaCipher:
    def __init__(self, bits=1024, conf=0):
        if conf != 0:
            self.private_key = bits
        else:
            self.bits = bits
            self.public_key, self.private_key = self.generate_keypair()



    def generate_keypair(self):
        p = self.generate_prime()
        q = self.generate_prime()

        n = p * q
        phi = (p - 1) * (q - 1)

        e = self.generate_coprime(phi)
        d = self.mod_inverse(e, phi)

        public_key = (n, e)
        private_key = (n, d)

        return public_key, private_key

    def generate_prime(self):
        while True:
            num = random.getrandbits(self.bits)
            num |= (1 << self.bits - 1) | 1

            if self.is_prime(num):
                return num

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    def generate_coprime(self, phi):
        e = random.randint(2, phi - 1)

        while math.gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)

        return e

    def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1

        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0

        return x1 + m0 if x1 < 0 else x1

    def encrypt(self, message):
        n, e = self.public_key
        encrypted_message = [pow(ord(char), e, n) for char in message]
        return ' '.join(str(i) for i in encrypted_message), self.public_key, self.private_key

    def decrypt(self, encrypted_message):
        encrypted_message = list(encrypted_message.split(' '))

        n, d = self.private_key
        decrypted_message = ''.join([chr(pow(int(char), d, n)) for char in encrypted_message])
        return decrypted_message

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

    def print_keys(self):
        print("Public Key (n, e):", self.public_key)
        print("Private Key (n, d):", self.private_key)

# Example usage:
if __name__ == "__main__":
    # Create an instance of the RSAEncryptorDecryptor class
    rsa_encryptor_decryptor = RsaCipher(bits=8)

    # Print public and private keys
    rsa_encryptor_decryptor.print_keys()

    # Message to be encrypted
    message = "Hello, RSA!"

    # Encrypt the message
    encrypted_message, pub_key, pr_key = rsa_encryptor_decryptor.encrypt(message)
    print("Encrypted Message:", encrypted_message)
    # Decrypt the message
    decrypted_message = rsa_encryptor_decryptor.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)
>>>>>>> 970b1648a4cea86e728aba5c185c8e8d0fd00d6b
