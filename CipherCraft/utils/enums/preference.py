from enum import Enum, auto
from typing import List
from enum import Enum, auto


# FIX VISUALS FOR QUESTIONARY
class VisualEnums(Enum):
    @classmethod
    def choices(cls):
        return [{'name': choice.__name__(), 'value': choice.value} for choice in cls]

    def __cmp__(self, other):
        return self.__name__() == other

    def __name__(self):
        return self.name.replace('_', ' ').title()


class Actions(VisualEnums):
    CLASSIC = auto()
    MODERN = auto()
    GENERATE_ASYMMETRIC_KEY = auto()
    EXIT = auto()


class AsymmetricAlgorithm(VisualEnums):
    RSA = auto()


class Operations(VisualEnums):
    ENCRYPT = auto()
    DECRYPT = auto()


# DEFINE THE KEY TYPE FOR ENCRYPTION
class EncryptionKey(VisualEnums):
    IMPORT_KEY = auto()
    INPUT_KEY = auto()
    GENERATE_RANDOM_KEY = auto()


# DEFINE THE DECRYPTION KEY METHOD
class DecryptionKey(VisualEnums):
    IMPORT_KEY = auto()
    INPUT_KEY = auto()
    WITHOUT_KEY = auto()


# DEFINE CRYPTANALYSIS OPTIONS
class Analyzing(VisualEnums):
    BRUTE_FORCE = auto()
    FREQUENCY_ANALYSIS = auto()


# DEFINE CLASSIC ALGORITHMS
class ClassicAlgorithms(VisualEnums):
    AFFINE = auto()
    CAESAR = auto()
    HILL = auto()
    MULTIPLICATIVE = auto()
    PERMUTATION = auto()
    TRANSPOSITION = auto()
    VIGENERE = auto()


# DEFINE MODERN ALGORITHMS
class ModernAlgorithms(VisualEnums):
    DES = auto()
    AES = auto()
    RC4 = auto()
    RSA = auto()


# OUTPUTTING THE PLAIN/CIPHER TEXT
class OutputMethod(VisualEnums):
    PRINT_ONLY = auto()
    SAVE_TO_FILE = auto()


# INPUTTING THE PLAIN/CIPHER TEXT
class InputMethod(VisualEnums):
    INPUT = auto()
    IMPORT_FROM_FILE = auto()


# DEFINE KEY METHOD
class KeyMethod(VisualEnums):
    KEY = auto()


# DEFINE KEY METHOD
class CryptAnalysis(VisualEnums):
    BRUTEFORCE = auto()
    FREQUENCYANALYSIS = auto()

