import unittest
import poetry_functions

class TestCountVowelPhonemes(unittest.TestCase):
	
    def test_count_vowel_phonemes_empty(self):
        """ Test count_vowel_phonemes on an empty list of lists. """

        actual = poetry_functions.count_vowel_phonemes([[]])
        expected = 0
        self.assertEqual(actual, expected)

    # Place your unit test definitions after this line.

    def test_count_vowel_phonemes_one(self):
        """ Test count_vowels for a list of list with one vowel phoneme. """

        actual = poetry_functions.count_vowel_phonemes([['D', 'AY1', 'N'], \
                                                        ['X', 'C', 'T']])
        expected = 1
        self.assertEqual(actual, expected, 'one vowel phoneme')

    def test_count_vowel_phonemes_multiple(self):
        """ Test count_vowels for a list of list with multiple vowel phonemes.
        """

        actual = poetry_functions.count_vowel_phonemes([['D', 'AY1', 'N'], \
                                                        ['AE1', 'C', 'T'], \
                                                        ['B', 'OW1', 'L']])
        expected = 3
        self.assertEqual(actual, expected, 'multiple vowel phonemes')

    def test_count_vowel_phonemes_no_vowels(self):
        """ Test count_vowels for a list of list with no vowel phonemes. """

        actual = poetry_functions.count_vowel_phonemes([['L', 'D', 'D'], \
                                                        ['Z', 'C', 'D'], \
                                                        ['P', 'H', 'D']])
        expected = 0
        self.assertEqual(actual, expected, 'no vowel phoneme')

# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
