import argparse
import os
import string


def get_hex_value(hex_file):
    # open file, read it, check if is hex64 true = return hex false = parse error
    with open(hex_file, 'r') as f:
        text = f.read()
    print(len(text))
    if len(text) < 64:
        return False
    if not all(c in string.hexdigits for c in text):
        return False
    return text
    

def get_key_value(key_file):
    # decypher file, open file, read it, check if is hex64 true = return hex false = parse error
    raise NotImplementedError('get_key_value not implemented yet')


def parse_args():
    parser = argparse.ArgumentParser(prog='ft_otp',
                                     description='generate a one time password')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', type=str, nargs='?',
                       default=None, metavar='HEX',
                       help='receives the path to a hexadecimal key and generate a .key file')
    group.add_argument('-k', type=str, nargs='?',
                       default=None, metavar='KEY',
                       help='receives the path to a .key file and generate a OTP password')

    parsed_args = parser.parse_args()
    if parsed_args.k is not None:
        if not os.path.isfile(parsed_args.k):
            parser.error('.key file not found!')
        parsed_args.k = get_key_value(parsed_args.k)
    if parsed_args.g is not None:
        if not os.path.isfile(parsed_args.g):
            parser.error('hex file not found!')
        parsed_args.g = get_hex_value(parsed_args.g)
        if not parsed_args.g:
            parser.error('key must be 64 hexadecimal characters.')

    return parsed_args


def generate_key(password_hex):
    raise NotImplementedError('generate_key not implemented yet')


def generate_otp(password_hex):
    raise NotImplementedError('generate_otp not implemented yet')


if __name__ == '__main__':
    args = parse_args()
    if args.g is not None:
        generate_key(args.g)
    elif args.k is not None:
        generate_otp(args.k)
