import CipherCraft.utils.enums.preference as pr
from CipherCraft.classic import caesar, hill,  affine, multiplicative, permutation, transposition, Vigenere
from CipherCraft.modern import rc4, des, aes, rsa
from CipherCraft.utils.Generators.keyGenerator import KeyGenerator
from CipherCraft.utils.Generators.logsHandler import LogsHandler
from CipherCraft.utils.keyParser import KeyParser


class Runner:
    def __init__(self):

        # INSTANCE FOR KEY GENERATOR
        self.key_gen = KeyGenerator()

        # INSTANCE FOR EVENTS LOGGER
        self.log_handler = LogsHandler()

        # INSTANCE FOR KEY PARSER
        self.key_parser = KeyParser()

        # A REFERENCE TO AN ANONYMOUS ALGORITHM
        self.algorithm = None

        # MAP ALL THE CRYPTOGRAPHY FUNCTIONS
        self.algorithm_mapping = {
            pr.Actions.CLASSIC.__name__(): {
                pr.ClassicAlgorithms.AFFINE.__name__(): affine.AffineCipher,
                pr.ClassicAlgorithms.CAESAR.__name__(): caesar.Caesar,
                pr.ClassicAlgorithms.HILL.__name__(): hill.HillCipher,
                pr.ClassicAlgorithms.MULTIPLICATIVE.__name__(): multiplicative.MultiplicativeCipher,
                pr.ClassicAlgorithms.PERMUTATION.__name__(): permutation.PermutationCipher,
                pr.ClassicAlgorithms.TRANSPOSITION.__name__(): transposition.TranspositionCipher,
                pr.ClassicAlgorithms.VIGENERE.__name__(): Vigenere.Vigenere,
            },
            pr.Actions.MODERN.__name__(): {
                pr.ModernAlgorithms.AES.__name__(): aes.AesCipher,
                pr.ModernAlgorithms.DES.__name__(): des.DesCipher,
                pr.ModernAlgorithms.RC4.__name__(): rc4.Rc4Cipher,
                pr.ModernAlgorithms.RSA.__name__(): rsa.RsaCipher.RsaExecutor,
            }
        }

        # MAP ASYMMETRIC ALGORITHMS FOR  KEY GEN
        self.asym_mappings = {
            pr.AsymmetricAlgorithm.RSA.__name__(): self.key_gen.Modern.rsa_key
        }

        # MAP SYMMETRIC ALGORITHMS FOR KEY GEN
        self.sym_mappings = {
            pr.Actions.CLASSIC.__name__(): {
                pr.ClassicAlgorithms.AFFINE.__name__(): self.key_gen.Classic.affine_key,
                pr.ClassicAlgorithms.CAESAR.__name__(): self.key_gen.Classic.caesar_key,
                pr.ClassicAlgorithms.HILL.__name__(): self.key_gen.Classic.hill_key,
                pr.ClassicAlgorithms.MULTIPLICATIVE.__name__(): self.key_gen.Classic.multiplicative_key,
                pr.ClassicAlgorithms.PERMUTATION.__name__(): self.key_gen.Classic.permutation_key,
                pr.ClassicAlgorithms.TRANSPOSITION.__name__(): self.key_gen.Classic.transposition_key,
                pr.ClassicAlgorithms.VIGENERE.__name__(): self.key_gen.Classic.vigenere_key,
            },
            pr.Actions.MODERN.__name__(): {
                pr.ModernAlgorithms.AES.__name__(): self.key_gen.Modern.aes_key,
                pr.ModernAlgorithms.DES.__name__(): self.key_gen.Modern.des_key,
                pr.ModernAlgorithms.RC4.__name__(): self.key_gen.Modern.rc4_key,
            }
        }

        # MAP FOR KEY PARSING
        self.key_parser_mappings = {
            pr.Actions.CLASSIC.__name__(): {
                pr.ClassicAlgorithms.AFFINE.__name__(): self.key_parser.parse_affine,
                pr.ClassicAlgorithms.CAESAR.__name__(): self.key_parser.parse_caesar,
                pr.ClassicAlgorithms.HILL.__name__(): self.key_parser.parse_hill,
                pr.ClassicAlgorithms.MULTIPLICATIVE.__name__(): self.key_parser.parse_multiplicative,
                pr.ClassicAlgorithms.PERMUTATION.__name__(): self.key_parser.parse_permutation,
                pr.ClassicAlgorithms.TRANSPOSITION.__name__(): self.key_parser.parse_transposition,
                pr.ClassicAlgorithms.VIGENERE.__name__(): self.key_parser.parse_vigenere,
            },
            pr.Actions.MODERN.__name__(): {
                pr.ModernAlgorithms.AES.__name__(): self.key_parser.parse_aes,
                pr.ModernAlgorithms.DES.__name__(): self.key_parser.parse_des,
                pr.ModernAlgorithms.RC4.__name__(): self.key_parser.parse_rc4,
                pr.ModernAlgorithms.RSA.__name__(): self.key_parser.parse_rsa,
            }
        }

    def __config(self, era, algorithm, conf):
        """
        This Function Set The Initiate The Desired Algorithm
        :param era: The Era Of The Algorithm
        :param algorithm: Name Of The Algo
        :param conf: Params To Pass To The Class INIT Function
        :return: None
        """
        self.algorithm = self.algorithm_mapping[era][algorithm](conf)

        # MAP THE OPERATIONS TO BE EXECUTED ON THE ALGORITHM
        self.operation_mapping = {
            pr.Operations.ENCRYPT.__name__(): self.algorithm.encrypt,
            pr.Operations.DECRYPT.__name__(): self.algorithm.decrypt
        }

    def parser(self, era, algorithm, key):
        """Function To Parse Keys"""
        return self.key_parser_mappings[era][algorithm](key)

    def generate(self, era, algorithm):
        """Function To Generate Key For Symmetric Algorithms"""
        return self.sym_mappings[era][algorithm]()

    def generate_asymmetric_key(self, algorithm, conf):
        """Function To Generate Asymmetric Key For Asymmetric Algorithm"""
        try:

            self.asym_mappings[algorithm](conf)
            self.log_handler.log_event(f"Successfully Generated A {conf}-bits Key And Saved To inventory/{algorithm.lower()}/")
            return "Success"
        finally:
            pass

    def run(self, era, algorithm, operation, source_text, key):
        """
                This Function Runs The Actions Of The Program
                :param key: The Key Or Config
                :param source_text: The Input Text/Message
                :param operation: What Actions To Perform
                :param era: The Era Of The Algorithm
                :param algorithm: Name Of The Algo
                :return: None
        """

        # Set The Configuration For The Algorithm Instance
        self.__config(era, algorithm, key)

        # Return The Value
        return self.operation_mapping[operation](source_text)