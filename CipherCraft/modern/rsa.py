import base64
import os
import random
import math
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from CipherCraft.utils.Generators.bigPrimeGenerator import big_prime_generator
from CipherCraft.utils.filesHandler import FilesHandler


class RsaCipher:
    def __init__(self):
        pass

    class RsaGenerator:
        def __init__(self, bits=1024, test=False):
            self.bits = bits
            self.file_handler = FilesHandler()
            self.public_key, self.private_key = self.generate_keypair()

            tmp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            public_key, private_key = self.generate_pem_keypair()
            if not test:
                self.file_handler.append_file(os.path.join(os.path.dirname(__file__),
                                                           '..', '..', 'inventory', 'rsa',
                                                           tmp + "rsa_pub.pem"
                                                           ), public_key)
                self.file_handler.append_file(os.path.join(os.path.dirname(__file__),
                                                           '..', '..', 'inventory', 'rsa',
                                                           tmp + "rsa_private.pem"
                                                           ), private_key)
            else:
                self.public_key, self.private_key = public_key, private_key

        def generate_pem_keypair(self):
            public_key = str(self.public_key[0]) + "@" + str(self.public_key[1])
            private_key = str(self.private_key[0]) + "@" + str(self.private_key[1])
            return _encode_to_pem(public_key.encode('utf8'), 'PUBLIC KEY'), _encode_to_pem(private_key.encode('utf8'),
                                                                                           'PRIVATE KEY')

        def generate_keypair(self):
            """Function To generate RSA key pairs"""
            p = big_prime_generator(self.bits)
            q = big_prime_generator(self.bits)

            n = p * q
            phi = (p - 1) * (q - 1)

            e = self.generate_coprime(phi)
            d = self.mod_inverse(e, phi)
            public_key = (n, e)
            private_key = (n, d)

            return public_key, private_key

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

        def get_public_key(self):
            return self.public_key

        def get_private_key(self):
            return self.private_key

    class RsaExecutor:
        def __init__(self, key):
            if type(key) == list:
                self.public_key = self.private_key = key

            elif type(key) == str:
                if 'PUBLIC KEY' in key:
                    key = _decode_from_pem(key, 'PUBLIC KEY')
                elif 'PRIVATE KEY' in key:
                    key = _decode_from_pem(key, 'PRIVATE KEY')
                else:
                    key = _decode_from_pem(key, None)
                key = key.decode('utf-8').split('@')
                self.public_key = self.private_key = ([int(i) for i in key])

        def encrypt(self, plaintext):
            """Function To Encrypt Text With RSA"""
            n, e = self.public_key
            ciphertext = [pow(ord(char), e, n) for char in plaintext]
            return ' '.join(str(i) for i in ciphertext)

        def decrypt(self, ciphertext):
            """Function To Decrypt RSA Encrypted Ciphertext"""
            ciphertext = list(map(int, ciphertext.split(' ')))
            n, d = self.private_key
            decrypted_text = ''.join([chr(pow(char, d, n)) for char in ciphertext])
            return decrypted_text


def _encode_to_pem(data, pem_type):
    """
    Encode binary data to PEM format.

    Parameters:
    - data: Bytes-like object to be encoded.
   - pem_type: A string specifying the type of PEM block (e.g., "CERTIFICATE", "RSA PRIVATE KEY").

    Returns:
    - PEM-encoded string.
    """
    b64_data = base64.b64encode(data).decode('ascii')
    pem_block = f"-----BEGIN {pem_type}-----\n{_insert_newlines(b64_data, 64)}\n-----END {pem_type}-----\n"
    return pem_block


def _decode_from_pem(pem_data, pem_type):
    """
    Decode PEM-encoded data.

    Parameters:
    - pem_data: PEM-encoded string.
    - pem_type: A string specifying the type of PEM block (e.g., "CERTIFICATE", "RSA PRIVATE KEY").

    Returns:
    - Decoded bytes.
    """
    pem_data = pem_data.strip()
    start_idx, end_idx = 0, len(pem_data) - 1
    b64_data = pem_data.replace('\n', '')
    if pem_type is not None:
        start_marker = f"-----BEGIN {pem_type}-----"
        end_marker = f"-----END {pem_type}-----"
        start_idx = pem_data.find(start_marker)
        end_idx = pem_data.find(end_marker)
        b64_data = pem_data[start_idx + len(start_marker):end_idx].replace('\n', '')
    if start_idx == -1 or end_idx == -1:
        raise ValueError(f"Invalid PEM data. Could not find start or end marker for {pem_type}.")

    decoded_data = base64.b64decode(b64_data)
    return decoded_data


def _insert_newlines(s, line_length):
    """Insert newline characters into a string at specified intervals."""
    return '\n'.join(s[i:i + line_length] for i in range(0, len(s), line_length))

