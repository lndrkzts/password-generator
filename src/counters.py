from typing import List

from src.constants import SPECIAL_CHARS_LIST, AMBIGUOUS_CHARS_LIST


def upper_count(string: List | str) -> int:
    return sum(1 for e in string if e.isupper())


def lower_count(string: List | str) -> int:
    return sum(1 for e in string if e.lower())


def lower_or_upper_count(string: List | str) -> int:
    return sum(1 for e in string if e.isupper() or e.islower())


def numbers_count(string: List | str) -> int:
    return sum(1 for e in string if e.isdigit())


def special_count(string: List | str) -> int:
    return sum(1 for e in string if e in SPECIAL_CHARS_LIST)


def ambiguous_check(string: List | str) -> bool:
    return any(e in AMBIGUOUS_CHARS_LIST for e in string)
