import argparse

from password_generator.passphrase import passphrase_generator

parser = argparse.ArgumentParser(description="Password Generator")

parser.add_argument("-w", "--words", type=int, help='Number of words', default=5)
parser.add_argument("-s", "--separator", type=str, help="Choose word separator", default='-')
parser.add_argument("-c", "--capitalize", action='store_true', help="Capitalize first letter", default=False)
parser.add_argument("-in", "--include-number", action='store_true', help="Include a random number", default=False)

args = parser.parse_args()

print("Generating passphrase...")

passphrase = passphrase_generator(
    words=args.words,
    separator=args.separator,
    capitalize=args.capitalize,
    include_number=args.include_number
)

print(passphrase)
