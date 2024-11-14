import unittest

from src.anagram import are_anagrams_array, are_anagrams_dict, are_anagrams_sorting


class TestAnagramMethods(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("listen", "silent", True),
            ("triangle", "integral", True),
            ("apple", "papel", True),
            ("rat", "car", False),
            ("night", "thing", True),
            ("dusty", "study", True),
            ("hello", "bello", False),
        ]

    def test_are_anagrams_sorting(self):
        for str1, str2, expected in self.test_cases:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(
                    are_anagrams_sorting(str1, str2),
                    expected,
                    f"Failed for {str1} and {str2}",
                )

    def test_are_anagrams_dict(self):
        for str1, str2, expected in self.test_cases:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(
                    are_anagrams_dict(str1, str2),
                    expected,
                    f"Failed for {str1} and {str2}",
                )

    def test_are_anagrams_array(self):
        for str1, str2, expected in self.test_cases:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(
                    are_anagrams_array(str1, str2),
                    expected,
                    f"Failed for {str1} and {str2}",
                )
