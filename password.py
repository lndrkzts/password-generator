import argparse

from password_generator.password import password_generator

parser = argparse.ArgumentParser(description="Password Generator")

parser.add_argument("-l", "--length", type=int, help='Password length', default=8)
parser.add_argument("-u", "--upper", action='store_true', help="Needs uppercase characters", default=False)
parser.add_argument("-lo", "--lower", action='store_true', help="Needs lowercase characters", default=False)
parser.add_argument("-n", "--number", action='store_true', help="Needs numbers", default=False)
parser.add_argument("-s", "--special", action='store_true', help="Needs specials characters", default=False)
parser.add_argument("-mn", "--min-numbers", type=int, help='Minimum amount of numbers', default=2)
parser.add_argument("-ms", "--min-special", type=int, help='minimum amount of specials characters', default=2)
parser.add_argument("-aa", "--avoid-ambiguous", action='store_true', help="Avoid ambiguous characters", default=False)

args = parser.parse_args()

print("Generating password...")

password = password_generator(
    length=args.length,
    needs_upper=args.upper,
    needs_lower=args.lower,
    needs_numbers=args.number,
    needs_special=args.special,
    min_numbers=args.min_numbers,
    min_special=args.min_special,
    avoid_ambiguous=args.avoid_ambiguous
)

print(password)
