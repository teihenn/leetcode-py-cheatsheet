"""
Test module for string operations.
"""

import unittest

from src.basic.string import extract_alphanumeric, reverse_string


class TestString(unittest.TestCase):
    """Test class for string operations"""

    def test_reverse_string_basic(self):
        """Test for basic string reversal"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_reverse_string_empty(self):
        """Test for empty string"""
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_single_char(self):
        """Test for single character string"""
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_string_japanese(self):
        """Test for Japanese string"""
        self.assertEqual(reverse_string("こんにちは"), "はちにんこ")

    def test_reverse_string_with_spaces(self):
        """Test for string with spaces"""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_extract_alphanumeric_basic(self):
        """Test for basic alphanumeric extraction"""
        self.assertEqual(extract_alphanumeric("Hello123"), "Hello123")
        self.assertEqual(extract_alphanumeric("Python3.9"), "Python39")

    def test_extract_alphanumeric_with_spaces(self):
        """Test for strings with spaces"""
        self.assertEqual(extract_alphanumeric("Hello World 123"), "HelloWorld123")
        self.assertEqual(extract_alphanumeric("   abc   123   "), "abc123")

    def test_extract_alphanumeric_with_special_chars(self):
        """Test for strings with special characters"""
        self.assertEqual(extract_alphanumeric("Hello@World!123"), "HelloWorld123")
        self.assertEqual(extract_alphanumeric("$#@123abc!?"), "123abc")

    def test_extract_alphanumeric_empty(self):
        """Test for empty string"""
        self.assertEqual(extract_alphanumeric(""), "")

    def test_extract_alphanumeric_no_alphanumeric(self):
        """Test for string with no alphanumeric characters"""
        self.assertEqual(extract_alphanumeric("@#$%^&*()"), "")

    def test_extract_alphanumeric_japanese_and_alphanumeric(self):
        """Test for string with Japanese and alphanumeric characters"""
        self.assertEqual(extract_alphanumeric("こんにちは123ABC"), "123ABC")
