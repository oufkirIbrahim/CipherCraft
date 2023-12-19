from enum import Enum


class Actions(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


class Mode(Enum):
    CLASSIC = "classic"
    MODERN = "modern"


class Algorithm(Enum):
    CAESAR = "caesar"
    MULTIPLICATIVE = "multiplicative"
    AFFINE = "affine"
    ALGORITHM4 = "permutation"
    ALGORITHM5 = "algorithm5"
    ALGORITHM6 = "algorithm6"
