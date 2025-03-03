"""
Unit tests for the set module.

This module contains tests for the set operations and functionality
demonstrated in the set module.
"""

import unittest

from src.basic.set import set_basics, set_comprehensions, set_operations


class TestSetBasics(unittest.TestCase):
    """Test cases for basic set operations."""

    def test_set_creation(self):
        """Test that sets are created correctly."""
        empty_set, numbers, fruits, mixed = set_basics()

        self.assertEqual(len(empty_set), 0)
        self.assertEqual(len(numbers), 5)
        self.assertEqual(len(fruits), 3)
        self.assertEqual(len(mixed), 3)

        # Test set contents
        self.assertEqual(numbers, {1, 2, 3, 4, 5})
        self.assertEqual(fruits, {"apple", "banana", "orange"})
        self.assertTrue(1 in mixed)
        self.assertTrue("hello" in mixed)
        self.assertTrue((1, 2) in mixed)

    def test_duplicate_removal(self):
        """Test that sets automatically remove duplicates."""
        # Create a set with duplicates
        with_duplicates = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}

        # Check that duplicates are removed
        self.assertEqual(with_duplicates, {1, 2, 3, 4})
        self.assertEqual(len(with_duplicates), 4)


class TestSetOperations(unittest.TestCase):
    """Test cases for common set operations."""

    def test_membership(self):
        """Test membership operations."""
        a, _ = set_operations()

        self.assertTrue(1 in a)
        self.assertTrue(5 in a)
        self.assertFalse(6 in a)
        self.assertFalse(0 in a)

    def test_add_remove(self):
        """Test adding and removing elements."""
        a = {1, 2, 3}

        # Test add
        a.add(4)
        self.assertEqual(a, {1, 2, 3, 4})

        # Adding existing element doesn't change the set
        a.add(3)
        self.assertEqual(a, {1, 2, 3, 4})

        # Test remove
        a.remove(4)
        self.assertEqual(a, {1, 2, 3})

        # Test discard (element exists)
        a.discard(3)
        self.assertEqual(a, {1, 2})

        # Test discard (element doesn't exist)
        a.discard(10)  # Should not raise an error
        self.assertEqual(a, {1, 2})

        # Test remove raises KeyError for non-existent element
        with self.assertRaises(KeyError):
            a.remove(10)

    def test_clear_and_pop(self):
        """Test clear and pop operations."""
        a = {1, 2, 3}

        # Test pop
        popped = a.pop()
        self.assertTrue(popped in {1, 2, 3})
        self.assertEqual(len(a), 2)

        # Test clear
        a.clear()
        self.assertEqual(len(a), 0)
        self.assertEqual(a, set())


class TestSetMathematicalOperations(unittest.TestCase):
    """Test cases for mathematical set operations."""

    def test_union(self):
        """Test union operation."""
        a = {1, 2, 3}
        b = {3, 4, 5}

        # Test operator
        self.assertEqual(a | b, {1, 2, 3, 4, 5})

        # Test method
        self.assertEqual(a.union(b), {1, 2, 3, 4, 5})

        # Union with multiple sets
        c = {5, 6, 7}
        self.assertEqual(a.union(b, c), {1, 2, 3, 4, 5, 6, 7})

    def test_intersection(self):
        """Test intersection operation."""
        a = {1, 2, 3, 4}
        b = {3, 4, 5, 6}

        # Test operator
        self.assertEqual(a & b, {3, 4})

        # Test method
        self.assertEqual(a.intersection(b), {3, 4})

        # Intersection with multiple sets
        c = {4, 5, 6, 7}
        self.assertEqual(a.intersection(b, c), {4})

    def test_difference(self):
        """Test difference operation."""
        a = {1, 2, 3, 4, 5}
        b = {4, 5, 6, 7}

        # Test operator
        self.assertEqual(a - b, {1, 2, 3})
        self.assertEqual(b - a, {6, 7})

        # Test method
        self.assertEqual(a.difference(b), {1, 2, 3})

        # Difference with multiple sets
        c = {3, 5, 7}
        self.assertEqual(a.difference(b, c), {1, 2})

    def test_symmetric_difference(self):
        """Test symmetric difference operation."""
        a = {1, 2, 3, 4, 5}
        b = {4, 5, 6, 7}

        # Test operator
        self.assertEqual(a ^ b, {1, 2, 3, 6, 7})

        # Test method
        self.assertEqual(a.symmetric_difference(b), {1, 2, 3, 6, 7})

    def test_subset_superset(self):
        """Test subset and superset operations."""
        a = {1, 2, 3, 4, 5}
        b = {1, 2, 3}
        c = {1, 2, 3, 4, 5, 6}

        # Test subset
        self.assertTrue(b.issubset(a))
        self.assertFalse(a.issubset(b))
        self.assertTrue(a.issubset(a))  # A set is a subset of itself

        # Test superset
        self.assertTrue(a.issuperset(b))
        self.assertFalse(b.issuperset(a))
        self.assertTrue(a.issuperset(a))  # A set is a superset of itself

        # Test with operators
        self.assertTrue(b <= a)  # subset
        self.assertTrue(b < a)  # proper subset
        self.assertTrue(a >= b)  # superset
        self.assertTrue(a > b)  # proper superset

        # Test relationships
        self.assertTrue(b < a < c)  # b is proper subset of a, a is proper subset of c


class TestSetComprehensions(unittest.TestCase):
    """Test cases for set comprehensions."""

    def test_basic_comprehension(self):
        """Test basic set comprehension."""
        squares, even_squares, _ = set_comprehensions()

        expected_squares = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
        self.assertEqual(squares, expected_squares)

        expected_even_squares = {0, 4, 16, 36, 64}
        self.assertEqual(even_squares, expected_even_squares)

    def test_duplicate_removal(self):
        """Test using set for duplicate removal."""
        numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
        unique_numbers = list(set(numbers))

        # Check that all unique elements are present
        self.assertEqual(set(unique_numbers), {1, 2, 3, 4, 5})

        # Check that the length is correct
        self.assertEqual(len(unique_numbers), 5)


class TestPracticalExamples(unittest.TestCase):
    """Test cases for practical examples of using sets."""

    def test_unique_words(self):
        """Test finding unique words in text."""
        text = "to be or not to be that is the question"
        unique_words = set(text.split())

        expected_words = {"to", "be", "or", "not", "that", "is", "the", "question"}
        self.assertEqual(unique_words, expected_words)

    def test_common_elements(self):
        """Test finding common elements between lists."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]

        common = set(list1).intersection(set(list2))
        self.assertEqual(common, {4, 5})

    def test_list_differences(self):
        """Test finding differences between lists."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]

        only_in_list1 = set(list1) - set(list2)
        only_in_list2 = set(list2) - set(list1)

        self.assertEqual(only_in_list1, {1, 2, 3})
        self.assertEqual(only_in_list2, {6, 7, 8})
