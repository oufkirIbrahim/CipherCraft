import CipherCraft.utils.enums.preference as pr
from CipherCraft.classic import caesar, hill,  affine, multiplicative, permutation, transposition, Vigenere
from CipherCraft.modern import rc4, des, aes, rsa


class Runner:
    def __init__(self):

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
                pr.ModernAlgorithms.RSA.__name__(): rsa.RsaCipher,
            }
        }

    def _config(self, era, algorithm, conf):
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
        self._config(era, algorithm, key)

        # Return The Value
        return self.operation_mapping[operation](source_text)