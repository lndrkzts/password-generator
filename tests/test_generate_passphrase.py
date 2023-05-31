import unittest

from password_generator import counters
from password_generator.passphrase import passphrase_generator


class TestGeneratePassphrase(unittest.TestCase):

    def test_default_passphrase_generation(self):
        passphrase = passphrase_generator()
        words_count = counters.words_count(passphrase)
        self.assertEqual(words_count, 5)

    def test_words(self):
        passphrase = passphrase_generator(words=8)
        words_count = counters.words_count(passphrase)
        self.assertEqual(words_count, 8)

    def test_separator(self):
        separator = '@'
        passphrase = passphrase_generator(words=5, separator=separator)
        separator_count = counters.char_count(passphrase, char=separator)
        self.assertEqual(separator_count, 4)

    def test_capitalize(self):
        passphrase = passphrase_generator(words=4, capitalize=True)
        upper_count = counters.upper_count(passphrase)
        self.assertEqual(upper_count, 4)

    def test_include_number(self):
        passphrase = passphrase_generator(include_number=True)
        numbers_count = counters.numbers_count(passphrase)
        self.assertEqual(numbers_count, 1)
