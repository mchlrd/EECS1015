import doctest


def remove_vowels(message: str) -> str:
    """
    Removes vowels (a, e, i, o, u) from the input string.

    Args:
        message (str): A string that may contain letters and spaces.

    Returns:
        str: A new string with vowels removed.

    Raises:
        AssertionError: If the input string contains digits.

    >>> remove_vowels("Python Programming")
    'Pythn Prgrmmng'
    >>> remove_vowels("abc")
    'bc'
    >>> remove_vowels("a")
    ''
    >>> remove_vowels("moving")
    'mvng'
    >>> remove_vowels("")
    ''
    >>> remove_vowels("APple")
    'Ppl'
    >>> remove_vowels(" ch erry")
    ' ch rry'
    >>> remove_vowels(" number 1 ")
    Traceback (most recent call last):
        ...
    AssertionError: Input string contains digits.
    """

    assert type(message) == str, 'invalid argument type'

    # Ensure the string does not contain digits
    if any(char.isdigit() for char in message):
        raise AssertionError("Input string contains digits.")

    if any (char in '{}' for char in message):
        raise AssertionError('Input is incorrect')

    vowels = "aeiouAEIOU"
    result = ''.join([char for char in message if char not in vowels])

    return result

doctest.testmod()