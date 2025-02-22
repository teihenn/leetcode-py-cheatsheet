"""
Basic dictionary operations in Python.

This module demonstrates fundamental dictionary operations including:
- Creating dictionaries
- Accessing and modifying elements
- Different methods for removing elements
- Common dictionary operations and methods
"""

# Examples of dictionary operations

# Creating a dictionary
fruits = {"apple": 100, "banana": 200, "orange": 150}

# Accessing elements
print(fruits["apple"])  # Output: 100

# Adding/Updating elements
fruits["grape"] = 300  # Adding new element
fruits["apple"] = 120  # Updating existing element
# fruits is now: {"apple": 120, "banana": 200, "orange": 150, "grape": 300}

# Methods for removing elements
# 1. Using del statement
del fruits["banana"]
# fruits is now: {"apple": 120, "orange": 150, "grape": 300}

# 2. Using pop() method - returns the removed value
price = fruits.pop("orange")  # price = 150
# fruits is now: {"apple": 120, "grape": 300}

# 3. Using popitem() method - removes and returns random item (last item in Python 3.7+)
last_item = fruits.popitem()  # last_item = ("grape", 300)
# fruits is now: {"apple": 120}

# 4. Using clear() method - removes all elements
fruits.clear()
# fruits is now: {}

# Dictionary operations
sample_dict = {"name": "Tanaka", "age": 25, "city": "Tokyo"}

# Checking if key exists
if "name" in sample_dict:
    print("Key 'name' exists")  # Will be printed

# Getting list of keys
keys = sample_dict.keys()  # dict_keys(['name', 'age', 'city'])

# Getting list of values
values = sample_dict.values()  # dict_values(['Tanaka', 25, 'Tokyo'])

# Getting key-value pairs
items = (
    sample_dict.items()
)  # dict_items([('name', 'Tanaka'), ('age', 25), ('city', 'Tokyo')])

# Getting value with default
score = sample_dict.get("score", 0)  # Returns 0 if key doesn't exist
