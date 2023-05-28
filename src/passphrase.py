import secrets
import string
import random

from random_word import RandomWords


def passphrase_generator(words: int = 5, separator: str = '-', capitalize: bool = False, include_number: bool = False):
    r = RandomWords()
    passphrase_list = [r.get_random_word() for _ in range(words)]

    if capitalize:
        passphrase_list = [p.capitalize() for p in passphrase_list]

    if include_number:
        passphrase_list[random.randint(0, len(passphrase_list))] += secrets.choice(string.digits)

    return f"{separator}".join(passphrase_list)
