"""Test cases for the anagram module."""
# mypy: ignore-errors

import unittest

from src.anagram import are_anagrams_array, are_anagrams_dict, are_anagrams_sorting


class TestAnagramMethods(unittest.TestCase):
    """Test cases for the anagram module."""

    def setUp(self):
        """Set up the test cases."""
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
        """Test the are_anagrams_sorting function."""
        for str1, str2, expected in self.test_cases:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(
                    are_anagrams_sorting(str1, str2),
                    expected,
                    f"Failed for {str1} and {str2}",
                )

    def test_are_anagrams_dict(self) -> None:
        """Test the are_anagrams_dict function."""
        for str1, str2, expected in self.test_cases:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(
                    are_anagrams_dict(str1, str2),
                    expected,
                    f"Failed for {str1} and {str2}",
                )

    def test_are_anagrams_array(self) -> None:
        """Test the are_anagrams_array function."""
        for str1, str2, expected in self.test_cases:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(
                    are_anagrams_array(str1, str2),
                    expected,
                    f"Failed for {str1} and {str2}",
                )
