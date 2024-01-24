from .enums import preference as pr


class KeySyntax:
    def __init__(self):
        self.syntax_mappings = {
            pr.Actions.CLASSIC.__name__(): {
                pr.ClassicAlgorithms.AFFINE.__name__(): 'List (invertible, integer) (use `,`)  Example: 5, 16',
                pr.ClassicAlgorithms.CAESAR.__name__(): 'Integer Example: 3 or C',
                pr.ClassicAlgorithms.HILL.__name__(): 'Invertible Squared Matrix (`,` for columns `:` for lines) Example: 1, 2 : 3, 4',
                pr.ClassicAlgorithms.MULTIPLICATIVE.__name__(): 'Invertible Integer Example: 7',
                pr.ClassicAlgorithms.PERMUTATION.__name__(): 'Shuffled Alphabets Example: ajklbcdefgihmnouvwpqrstxyz',
                pr.ClassicAlgorithms.TRANSPOSITION.__name__(): 'List Of Shuffled Indices (use `,`) : 4,1,2,3',
                pr.ClassicAlgorithms.VIGENERE.__name__(): 'String of Alphabets Example: UITZZ'
            },
            pr.Actions.MODERN.__name__(): {
                pr.ModernAlgorithms.DES.__name__(): 'Hex Code  Of Fixed Size [16] Example: 1DE567890A234BCFG',
                pr.ModernAlgorithms.AES.__name__(): 'Hex Code  Of Fixed Size [32] Example: 234BCFG1DE567890A234BCFG1DE567890A',
                pr.ModernAlgorithms.RC4.__name__(): 'String Of Printable Example: 15II-@S&AAZS;~,E',
                pr.ModernAlgorithms.RSA.__name__(): 'Tuple (`n`, `e` or `d`) Example: 221, 35 or [PEM format]'
            }
        }

    def get_syntax(self, era, algorithm):
        """Function returns Algorithm syntax"""
        return self.syntax_mappings[era][algorithm]
