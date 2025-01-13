"""
Module for string manipulation operations.
"""


def reverse_string(text: str) -> str:
    """
    Returns the reversed string

    Args:
        text (str): The string to be reversed

    Returns:
        str: The reversed string

    Examples:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]


def extract_alphanumeric(text: str) -> str:
    """
    Extracts only alphanumeric characters from the given string

    Args:
        text (str): The input string

    Returns:
        str: String containing only alphanumeric characters

    Examples:
        >>> extract_alphanumeric("Hello, World! 123")
        'HelloWorld123'
        >>> extract_alphanumeric("@#$% abc 123")
        'abc123'
    """
    return "".join(char for char in text if char.isalnum())
