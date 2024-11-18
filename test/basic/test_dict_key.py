"""Demonstrates which types of objects can be used as dictionary keys in Python."""

# mypy: ignore-errors
# ruff: noqa

import unittest


class TestDictKey(unittest.TestCase):
    """Test cases demonstrating valid and invalid dictionary keys in Python."""

    def test_immutable_keys(self):
        """Test basic immutable types as dictionary keys.

        Demonstrates that basic immutable types can be used as dictionary keys:
        - strings
        - integers
        - floats
        These types are hashable and their values cannot be changed after creation.
        """
        test_dict = {"string_key": "value", 42: "value", 3.14: "value"}
        self.assertIn("string_key", test_dict)
        self.assertIn(42, test_dict)
        self.assertIn(3.14, test_dict)

    def test_tuple_keys(self):
        """Test tuples as dictionary keys.

        Demonstrates that tuples can be used as dictionary keys because:
        - Tuples are immutable
        - If all elements in the tuple are hashable, the tuple itself is hashable
        - Nested tuples are also valid as long as all nested elements are hashable
        """
        test_dict = {(1, 2): "value", (1, "two", 3.0): "another value"}
        self.assertIn((1, 2), test_dict)
        self.assertIn((1, "two", 3.0), test_dict)

    def test_mutable_keys_fail(self):
        """Test that mutable types cannot be used as dictionary keys.

        Demonstrates that mutable types raise TypeError when used as keys:
        - Lists: mutable sequences
        - Dictionaries: mutable mappings
        - Sets: mutable collections

        This is because mutable objects can change after being used as keys,
        which would break the dictionary's ability to look up values.
        """
        with self.assertRaises(TypeError):
            test_dict = {[1, 2, 3]: "value"}

        with self.assertRaises(TypeError):
            test_dict = {{"key": "value"}: "value"}

        with self.assertRaises(TypeError):
            test_dict = {set([1, 2, 3]): "value"}

    def test_custom_object_keys(self):
        """Test custom objects as dictionary keys.

        Demonstrates that custom objects can be used as dictionary keys if they:
        1. Implement __hash__ method: defines how the object should be hashed
        2. Implement __eq__ method: defines how objects should be compared

        These methods must ensure that:
        - Objects that are equal have the same hash value
        - Hash value remains constant during the object's lifetime
        """

        class CustomKey:
            def __init__(self, value):
                self.value = value

            def __hash__(self):
                return hash(self.value)

            def __eq__(self, other):
                return isinstance(other, CustomKey) and self.value == other.value

        obj1 = CustomKey(1)
        obj2 = CustomKey(2)
        test_dict = {obj1: "Object 1", obj2: "Object 2"}

        self.assertIn(obj1, test_dict)
        self.assertIn(obj2, test_dict)

    def test_hashability(self):
        """Test hashability of different objects.

        Demonstrates the fundamental requirement for dictionary keys:
        - Only hashable objects can be dictionary keys
        - Hashable means the object has a hash value that never changes

        Built-in immutable types are hashable:
        - strings, numbers, tuples

        Built-in mutable types are not hashable:
        - lists, sets, dictionaries
        """
        self.assertTrue(hash("test"))
        self.assertTrue(hash((1, 2, 3)))

        with self.assertRaises(TypeError):
            hash([1, 2, 3])

        with self.assertRaises(TypeError):
            hash(set([1, 2, 3]))
