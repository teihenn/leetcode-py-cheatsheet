"""
OrderedDict operations in Python.

This module demonstrates the usage of collections.OrderedDict and its differences from regular dict:
- OrderedDict maintains the order of item insertion
- Key differences between OrderedDict and regular dict
- Common OrderedDict operations and methods
"""

from collections import OrderedDict

# When to use OrderedDict vs regular dict:
# Use OrderedDict when:
# - Order of insertion needs to be preserved and is meaningful
# - You need equality comparisons that consider order
# - You need to move items to the start/end of the dictionary

# Use regular dict when:
# - Order is not important
# - Memory efficiency is a concern
# - You're using Python 3.7+ and just need basic insertion order preservation
#   (regular dict maintains insertion order since Python 3.7)

# Key differences between dict and OrderedDict:
# 1. Order matters in equality comparison
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)  # Output: True (order doesn't matter for regular dict)

odict1 = OrderedDict([("a", 1), ("b", 2)])
odict2 = OrderedDict([("b", 2), ("a", 1)])
print(odict1 == odict2)  # Output: False (order matters for OrderedDict)

# 2. Memory usage
# OrderedDict uses more memory than regular dict as it maintains a doubly-linked list

# Creating an OrderedDict
# OrderedDict remembers the order in which keys were inserted
ordered_fruits = OrderedDict()
ordered_fruits["apple"] = 100
ordered_fruits["banana"] = 200
ordered_fruits["orange"] = 150
# Output: OrderedDict([('apple', 100), ('banana', 200), ('orange', 150)])

# Creating from list of tuples
items = [("a", 1), ("b", 2), ("c", 3)]
ordered_dict = OrderedDict(items)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Common operations (similar to regular dict)
ordered_fruits["grape"] = 300  # Adding new element
del ordered_fruits["apple"]  # Removing element
price = ordered_fruits.pop("banana")  # Removing and returning value

# OrderedDict specific operations
# Moving element to end
ordered_dict.move_to_end("a")
# Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Moving element to beginning
ordered_dict.move_to_end("a", last=False)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
