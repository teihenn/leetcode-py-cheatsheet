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


def extract_alphanumeric(s: str) -> str:
    """
    Extracts only alphanumeric characters from the given string

    Args:
        s (str): The input string

    Returns:
        str: String containing only alphanumeric characters

    Examples:
        >>> extract_alphanumeric("Hello, World! 123")
        'HelloWorld123'
        >>> extract_alphanumeric("@#$% abc 123")
        'abc123'
        >>> extract_alphanumeric("こんにちは123ABCワールド")
        '123ABC'
    """
    # isascii() ensures we only get ASCII characters (0-127),
    # excluding Unicode characters like Japanese, Emoji, etc.
    return "".join(c for c in s if c.isascii() and c.isalnum())
