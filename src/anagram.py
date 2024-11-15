"""
This module contains functions to determine if two strings are anagrams.
"""

from collections import defaultdict


# Method 1: Using Sorting
def are_anagrams_sorting(str1, str2):
    """
    Determines if two strings are anagrams by sorting.
    """
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters of both strings match
    return sorted(str1) == sorted(str2)


# Method 2: Using Character Count with defaultdict for both strings
def are_anagrams_dict(str1, str2):
    """Determines if two strings are anagrams by counting characters with defaultdict for both strings."""
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Early return if lengths do not match
    if len(str1) != len(str2):
        return False

    # Count characters in both strings
    char_count1 = defaultdict(int)
    char_count2 = defaultdict(int)

    for char in str1:
        char_count1[char] += 1
    for char in str2:
        char_count2[char] += 1

    # Compare both dictionaries
    return char_count1 == char_count2


# Method 3: Using Character Count with Array (assuming ASCII characters)
def are_anagrams_array(str1, str2):
    """Determines if two strings are anagrams by counting characters with an array.

    Assumes only ASCII characters.
    """
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Early return if lengths do not match
    if len(str1) != len(str2):
        return False

    # Initialize an array for 128 ASCII characters
    char_count = [0] * 128

    # Increment counts for str1 and decrement for str2
    for char in str1:
        char_count[ord(char)] += 1
    for char in str2:
        char_count[ord(char)] -= 1

    # If all counts are zero, they are anagrams
    return all(count == 0 for count in char_count)
