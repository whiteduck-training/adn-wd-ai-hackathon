def reverse_string(word: str) -> str:
    """
    Reverses the given string and capitalizes the first letter of the reversed string.

    Args:
        word (str): The string to be reversed.

    Returns:
        str: The reversed string with the first letter capitalized.
    """
    reversed_word = word[::-1]
    return reversed_word
