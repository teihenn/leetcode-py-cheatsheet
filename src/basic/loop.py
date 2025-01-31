"""
Collection of basic loop patterns using Python's range
"""

from typing import List


def basic_forward_loop() -> List[int]:
    """
    Basic forward loop
    range(n): generates a sequence from 0 to n-1
    """
    result = []
    for i in range(5):  # 0, 1, 2, 3, 4
        result.append(i)
    return result


def reverse_loop() -> List[int]:
    """
    Reverse loop
    range(start, end, step): generates a sequence from start to end with step interval
    """
    result = []
    for i in range(4, -1, -1):  # 4, 3, 2, 1, 0
        result.append(i)
    return result


def step_loop() -> List[int]:
    """
    Loop with step
    Generates a sequence with step interval of 2
    """
    result = []
    for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
        result.append(i)
    return result


def loop_with_index(arr: List[str]) -> List[tuple]:
    """
    Get index and element simultaneously
    Using enumerate() to get both index and value
    """
    result = []
    for i, value in enumerate(arr):
        result.append((i, value))
    return result


def range_with_start_end() -> List[int]:
    """
    Loop with specified start and end values
    range(start, end): generates a sequence from start to end-1
    """
    result = []
    for i in range(2, 7):  # 2, 3, 4, 5, 6
        result.append(i)
    return result
