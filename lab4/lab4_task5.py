import doctest

def xor_operator(a: bool, b: bool) -> bool:
    '''
    Xor operator results in True if and only if one of the boolean variables is True.

    Parameters:
    - a (bool): First boolean argument
    - b (bool): Second boolean argument
    Returns:
    - bool: True if one of the boolean operators is true and false otherwise
    Examples:
    >>> xor_operator(True, False)
    True
    >>> xor_operator(False, True)
    True
    >>> xor_operator(True, True)
    False
    >>> xor_operator(False, False)
    False
    >>> xor_operator('True', False)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type of a
    >>> xor_operator(True, 'False')
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type of b
    '''
    assert type(a) == bool, 'invalid data type of a'
    assert type(b) == bool, 'invalid data type of b'

    result = (a or b) and not(a and b)

    return result

doctest.testmod()
