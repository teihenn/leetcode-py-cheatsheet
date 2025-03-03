"""
Module demonstrating sorting methods in Python.

This module explains the usage and differences between the built-in
sort() method and sorted() function.
"""

from typing import Callable, Iterable, Optional


# List sort() method - modifies the original list (in-place operation)
def sort_list(
    numbers: list, reverse: bool = False, key: Optional[Callable] = None
) -> list:
    """
    Sort a list in-place using the sort() method.

    Args:
        numbers: List to be sorted
        reverse: If True, sort in descending order
        key: Function to extract comparison key

    Returns:
        The sorted list (same object as input)
    """
    numbers.sort(reverse=reverse, key=key)
    return numbers


# sorted() function - returns a new sorted list (non-destructive operation)
def get_sorted_list(
    iterable: Iterable, reverse: bool = False, key: Optional[Callable] = None
) -> list:
    """
    Return a new sorted list from an iterable using the sorted() function.

    Args:
        iterable: Any iterable object to be sorted
        reverse: If True, sort in descending order
        key: Function to extract comparison key

    Returns:
        A new sorted list
    """
    return sorted(iterable, reverse=reverse, key=key)
