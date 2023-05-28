import secrets
import string
import random
from typing import List

SPECIAL_CHARS = "!@#$%^&*"
SPECIAL_CHARS_LIST = list(SPECIAL_CHARS)
AMBIGUOUS_CHARS_LIST = ["i", "j", "l", "o", "I", "J", "L", "O", "1", "0"]


def password_generator(length: int, needs_upper: bool, needs_lower: bool, needs_numbers: bool, needs_special: bool,
                       min_numbers: int, min_special: int, avoid_ambiguous: bool) -> string:
    chars = ""

    if needs_upper:
        chars += string.ascii_uppercase
    if needs_lower:
        chars += string.ascii_lowercase
    if needs_numbers:
        chars += string.digits
    if needs_special:
        chars += SPECIAL_CHARS

    while True:
        password_list = [secrets.choice(chars) for _ in range(length)]
        is_valid = _validate_password(password_list, needs_upper, needs_lower, needs_numbers, needs_special,
                                      min_numbers, min_special, avoid_ambiguous)

        if is_valid:
            break

    random.shuffle(password_list)
    password = "".join(password_list)

    return "".join(password)


def _validate_password(password_list: List, needs_upper: bool, needs_lower: bool, needs_numbers: bool,
                       needs_special: bool, min_numbers: int, min_special: int, avoid_ambiguous: bool) -> bool:
    upper_count = sum(1 for e in password_list if e.isupper())
    lower_count = sum(1 for e in password_list if e.islower())
    numbers_count = sum(1 for e in password_list if e.isdigit())
    special_count = sum(1 for e in password_list if e in SPECIAL_CHARS_LIST)
    ambiguous_bool = any(e in AMBIGUOUS_CHARS_LIST for e in password_list)

    if (needs_upper and (upper_count == 0)) or \
            (needs_lower and (lower_count == 0)) or \
            (needs_numbers and (numbers_count < min_numbers)) or \
            (needs_special and (special_count < min_special)) or \
            (avoid_ambiguous and not ambiguous_bool):
        return False
    return True