"""
Python set operations and usage examples.

This module demonstrates the basic operations and common use cases for Python sets.
Sets are unordered collections of unique elements, useful for membership testing,
removing duplicates, and mathematical set operations.
"""


def set_basics():
    """Demonstrate basic set creation and properties."""
    # Creating sets
    empty_set = set()  # Empty set
    numbers = {1, 2, 3, 4, 5}  # Set of numbers
    fruits = {"apple", "banana", "orange"}  # Set of strings
    mixed = {1, "hello", (1, 2)}  # Set with different types

    # Sets cannot contain mutable objects like lists or dictionaries
    # This would raise TypeError: unhashable type: 'list'
    # invalid_set = {[1, 2], 3}

    # Sets automatically remove duplicates
    with_duplicates = {1, 2, 2, 3, 3, 3}
    print(f"Set with duplicates: {with_duplicates}")  # {1, 2, 3}

    # Check length
    print(f"Number of elements: {len(fruits)}")

    return empty_set, numbers, fruits, mixed


def set_operations():
    """Demonstrate common set operations."""
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    # Membership testing
    print(f"Is 3 in set a? {3 in a}")
    print(f"Is 6 in set a? {6 in a}")

    # Adding elements
    c = a.copy()
    c.add(6)  # Add a single element
    print(f"After adding 6: {c}")

    # Removing elements
    c.remove(6)  # Raises KeyError if element doesn't exist
    print(f"After removing 6: {c}")

    c.discard(10)  # No error if element doesn't exist

    # Pop - removes and returns an arbitrary element
    popped = c.pop()
    print(f"Popped element: {popped}, Set after pop: {c}")

    # Clear - removes all elements
    d = a.copy()
    d.clear()
    print(f"After clear: {d}")

    return a, b


def set_mathematical_operations():
    """Demonstrate mathematical set operations."""
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    # Union (OR): elements in either set
    union1 = a | b
    print(f"Union: {union1}")
    # Using method syntax (alternative)
    print(f"Union (using method): {a.union(b)}")

    # Intersection (AND): elements in both sets
    intersection1 = a & b
    print(f"Intersection: {intersection1}")
    # Using method syntax (alternative)
    print(f"Intersection (using method): {a.intersection(b)}")

    # Difference: elements in first set but not in second
    difference1 = a - b
    print(f"Difference (a - b): {difference1}")
    # Using method syntax (alternative)
    print(f"Difference (using method): {a.difference(b)}")

    # Symmetric difference: elements in either set, but not in both
    sym_diff1 = a ^ b
    print(f"Symmetric difference: {sym_diff1}")
    # Using method syntax (alternative)
    print(f"Symmetric difference (using method): {a.symmetric_difference(b)}")

    # Subset and superset
    c = {1, 2}
    print(f"Is c subset of a? {c.issubset(a)}")
    print(f"Is a superset of c? {a.issuperset(c)}")

    return union1, intersection1, difference1, sym_diff1


def set_comprehensions():
    """Demonstrate set comprehensions."""
    # Basic set comprehension
    squares = {x**2 for x in range(10)}
    print(f"Squares: {squares}")

    # Conditional set comprehension
    even_squares = {x**2 for x in range(10) if x % 2 == 0}
    print(f"Even squares: {even_squares}")

    # Using set to remove duplicates from a list
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    unique_numbers = list(set(numbers))
    print(f"Original list: {numbers}")
    print(f"Unique numbers: {unique_numbers}")

    return squares, even_squares, unique_numbers
