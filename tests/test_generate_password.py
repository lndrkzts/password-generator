import unittest

from password_generator import counters
from password_generator.password import password_generator


class TestGeneratePassword(unittest.TestCase):

    def test_default_password_generation(self):
        password = password_generator()

        chars_count = counters.lower_or_upper_count(password)
        numbers_count = counters.numbers_count(password)
        special_count = counters.special_count(password)

        self.assertEquals(len(password), 8)
        self.assertTrue(chars_count >= 1)
        self.assertTrue(numbers_count >= 2)
        self.assertTrue(special_count >= 2)

    def test_lower_and_upper_with_false_value(self):
        password = password_generator(needs_upper=False, needs_lower=False)

        upper_count = counters.upper_count(password)
        lower_count = counters.lower_count(password)

        self.assertTrue(upper_count == 0)
        self.assertTrue(lower_count >= 2)

    def test_length(self):
        password = password_generator(length=20)
        self.assertEquals(len(password), 20)

    def test_needs_upper(self):
        password = password_generator(needs_upper=True)
        upper_count = counters.upper_count(password)
        self.assertTrue(upper_count > 0)

    def test_needs_lower(self):
        password = password_generator(needs_lower=True)
        lower_count = counters.lower_count(password)
        self.assertTrue(lower_count > 0)

    def test_needs_numbers(self):
        password = password_generator(length=12, needs_numbers=True, min_numbers=3)
        numbers_count = counters.numbers_count(password)
        self.assertTrue(numbers_count >= 3)

    def test_needs_special(self):
        password = password_generator(length=12, needs_special=True, min_special=3)
        special_count = counters.special_count(password)
        self.assertTrue(special_count >= 3)

    def test_avoid_ambiguous(self):
        password = password_generator(length=12, needs_upper=True, needs_lower=True, needs_numbers=True,
                                      needs_special=True, avoid_ambiguous=True)
        has_ambiguous = counters.ambiguous_check(password)
        self.assertTrue(not has_ambiguous)
