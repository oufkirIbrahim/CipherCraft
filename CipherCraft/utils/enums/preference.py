from enum import Enum, auto
from typing import List
from enum import Enum, auto


# FIX VISUALS FOR QUESTIONARY
class VisualEnums(Enum):
    @classmethod
    def choices(cls):
        return [{'name': choice.name.replace('_', ' ').title(), 'value': choice.value} for choice in cls]


class Actions(VisualEnums):
    CLASSIC = auto()
    MODERN = auto()
    EXIT = auto()


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
    CAESAR = auto()
    AFFINE = auto()
    VIGENERE = auto()
    MULTIPLICATIVE = auto()


# DEFINE MODERN ALGORITHMS
class ModernAlgorithms(VisualEnums):
    AES = auto()


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