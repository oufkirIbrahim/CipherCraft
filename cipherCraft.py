from argparse import ArgumentParser, Namespace
from CipherCraft.utils.cryptoHandler import CryptoHandlerFactory
from CipherCraft.utils.enums import Actions,Algorithm,Mode


def main():
    parser = ArgumentParser(description='Encrypt data using different algorithms.')
    parser.add_argument("-a","--action", type=Actions, default=Actions.ENCRYPT, help="Specify action (encrypt or decrypt)")
    parser.add_argument("-m","--mode",type=Mode, default=Mode.CLASSIC,help="Specify encryption type (classic or modern)")
    parser.add_argument("-alg","--algorithm",type=Algorithm, default=Algorithm.CAESAR,help="help='Specify encryption algorithm")
    parser.add_argument("-d","--data", required=True, help="Specify data to process")
    args: Namespace = parser.parse_args()

    proc = CryptoHandlerFactory.create_handler(args.mode)
    if args.action == Actions.ENCRYPT:
        proc.encrypt(args.data,args.algorithm)
    elif args.action == Actions.DECRYPT:
        proc.decrypt(args.data,args.algorithm)

if __name__ == "__main__":
    main()
