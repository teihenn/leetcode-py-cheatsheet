"""Unit tests for loop patterns using Python's range function.
Each test case validates the expected output against the actual output
from the corresponding function in the loop module.
"""

import unittest

from src.basic.loop import (
    basic_forward_loop,
    loop_with_index,
    range_with_start_end,
    reverse_loop,
    step_loop,
)


class TestLoop(unittest.TestCase):
    """Test cases for various loop patterns using range function."""

    def test_basic_forward_loop(self):
        """Test basic forward loop from 0 to 4"""
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(basic_forward_loop(), expected)

    def test_reverse_loop(self):
        """Test reverse loop from 4 to 0"""
        expected = [4, 3, 2, 1, 0]
        self.assertEqual(reverse_loop(), expected)

    def test_step_loop(self):
        """Test loop with step interval of 2"""
        expected = [0, 2, 4, 6, 8]
        self.assertEqual(step_loop(), expected)

    def test_loop_with_index(self):
        """Test loop with index using enumerate"""
        test_input = ["a", "b", "c"]
        expected = [(0, "a"), (1, "b"), (2, "c")]
        self.assertEqual(loop_with_index(test_input), expected)

    def test_range_with_start_end(self):
        """Test loop with specified start and end values"""
        expected = [2, 3, 4, 5, 6]
        self.assertEqual(range_with_start_end(), expected)
