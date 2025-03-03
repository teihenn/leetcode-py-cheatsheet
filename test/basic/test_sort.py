"""
Unit tests for the sort module.
"""

import unittest

from src.basic.sort import get_sorted_list, sort_list


class TestSortMethods(unittest.TestCase):
    """Test cases for the sorting functions."""

    def test_sort_list_basic(self):
        """Test basic sorting with sort_list function."""
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        result = sort_list(numbers)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        # Verify it's the same object (in-place sorting)
        self.assertIs(result, numbers)

    def test_sort_list_reverse(self):
        """Test reverse sorting with sort_list function."""
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        result = sort_list(numbers, reverse=True)
        self.assertEqual(result, [9, 6, 5, 4, 3, 2, 1, 1])

    def test_sort_list_with_key(self):
        """Test sorting with a key function."""
        numbers = [-3, 1, -4, 1, 5, -9, 2, 6]
        result = sort_list(numbers, key=abs)
        self.assertEqual(result, [1, 1, 2, -3, -4, 5, 6, -9])

    def test_get_sorted_list_basic(self):
        """Test basic sorting with get_sorted_list function."""
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        result = get_sorted_list(numbers)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        # Verify it's a new object (non-destructive sorting)
        self.assertIsNot(result, numbers)
        # Original list should be unchanged
        self.assertEqual(numbers, [3, 1, 4, 1, 5, 9, 2, 6])

    def test_get_sorted_list_reverse(self):
        """Test reverse sorting with get_sorted_list function."""
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        result = get_sorted_list(numbers, reverse=True)
        self.assertEqual(result, [9, 6, 5, 4, 3, 2, 1, 1])
        # Original list should be unchanged
        self.assertEqual(numbers, [3, 1, 4, 1, 5, 9, 2, 6])

    def test_get_sorted_list_with_key(self):
        """Test sorting with a key function."""
        words = ["apple", "Banana", "cherry", "Date"]
        result = get_sorted_list(words, key=str.lower)
        self.assertEqual(result, ["apple", "Banana", "cherry", "Date"])

    def test_get_sorted_list_with_tuple(self):
        """Test sorting a tuple."""
        data = (3, 1, 4, 1, 5, 9, 2, 6)
        result = get_sorted_list(data)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
        # Result should be a list, not a tuple
        self.assertIsInstance(result, list)

    def test_get_sorted_list_with_string(self):
        """Test sorting a string."""
        text = "python"
        result = get_sorted_list(text)
        self.assertEqual(result, ["h", "n", "o", "p", "t", "y"])

    def test_sort_list_of_dicts(self):
        """Test sorting a list of dictionaries."""
        people = [
            {"name": "Tanaka", "age": 30},
            {"name": "Sato", "age": 25},
            {"name": "Suzuki", "age": 40},
        ]
        result = get_sorted_list(people, key=lambda x: x["age"])
        expected = [
            {"name": "Sato", "age": 25},
            {"name": "Tanaka", "age": 30},
            {"name": "Suzuki", "age": 40},
        ]
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test sorting an empty list."""
        empty_list = []
        self.assertEqual(sort_list(empty_list), [])
        self.assertEqual(get_sorted_list(empty_list), [])

    def test_already_sorted(self):
        """Test sorting an already sorted list."""
        sorted_list = [1, 2, 3, 4, 5]
        self.assertEqual(sort_list(sorted_list), [1, 2, 3, 4, 5])
        self.assertEqual(get_sorted_list(sorted_list), [1, 2, 3, 4, 5])

    def test_all_same_elements(self):
        """Test sorting a list with all identical elements."""
        same_elements = [7, 7, 7, 7]
        self.assertEqual(sort_list(same_elements), [7, 7, 7, 7])
        self.assertEqual(get_sorted_list(same_elements), [7, 7, 7, 7])
