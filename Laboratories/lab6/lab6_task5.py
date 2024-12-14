import doctest
def reverse_str(data: str) -> str:
    '''


    Args:
        data: message to be inverted

    Returns: inverted data

    >>> reverse_str('d')
    'd'
    >>> reverse_str('z')
    'z'
    >>> reverse_str('f')
    'f'
    >>> reverse_str('f ')
    ' f'

    '''

    assert type(data) == str, 'Invalid argument type'
    data = data[::-1]

    return data


doctest.testmod()