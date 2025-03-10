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

    Time Complexity:
        O(n) where n is the length of the string

    Space Complexity:
        O(n) as a new reversed string is created

    Examples:
        >>> reverse_string("hello")
        'olleh'
    """
    # text[::-1]: String slicing with step -1
    # - Start: empty (default: beginning of string)
    # - End: empty (default: end of string)
    # - Step: -1 (traverse backwards)
    # Example: "hello" -> "olleh"
    return text[::-1]


def reverse_string_builtin(text: str) -> str:
    """
    Returns the reversed string using Python's built-in reversed() function

    Args:
        text (str): The string to be reversed

    Returns:
        str: The reversed string

    Time Complexity:
        O(n) where n is the length of the string

    Space Complexity:
        O(n) as a new reversed string is created

    Examples:
        >>> reverse_string_builtin("hello")
        'olleh'
    """
    # reversed(sequence): creates an iterator that yields elements in reverse order
    #                    (works with sequences like str, list, tuple, but not with unordered iterables like set)
    # "".join(): concatenates iterator elements into a single string using empty string as separator
    # example: "hello" -> iterator('o','l','l','e','h') -> "olleh"
    return "".join(reversed(text))


def extract_alphanumeric(s: str) -> str:
    """
    Extracts only alphanumeric characters from the given string

    Args:
        s (str): The input string

    Returns:
        str: String containing only alphanumeric characters

    Time Complexity:
        O(n) where n is the length of the string, as we check each character

    Space Complexity:
        O(n) in the worst case (if all characters are alphanumeric and ASCII)

    Examples:
        >>> extract_alphanumeric("Hello, World! 123")
        'HelloWorld123'
        >>> extract_alphanumeric("@#$% abc 123")
        'abc123'
        >>> extract_alphanumeric("こんにちは123ABCワールド")
        '123ABC'
    """
    # isalnum() alone would include Unicode alphanumeric characters (like '１２３４５' or 'ＡＢＣＤＥ')
    # isascii() ensures we only get ASCII characters (0-127),
    # excluding Unicode characters like Japanese, Emoji, etc.
    return "".join(c for c in s if c.isascii() and c.isalnum())
