from enum import Enum

class Actions(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"

class Mode(Enum):
    CLASSIC = "classic"
    MODERN = "modern"

class Algorithm(Enum):
    CAESAR = "caeser"
    ALGORITHM2 = "algorithm2"
    ALGORITHM3 = "algorithm3"
    ALGORITHM4 = "algorithm4"
    ALGORITHM5 = "algorithm5"
    ALGORITHM6 = "algorithm6"
