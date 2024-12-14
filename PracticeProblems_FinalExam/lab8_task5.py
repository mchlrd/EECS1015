def reverse_str(message: str) -> str:
    '''

    Args:
        message:

    Returns:
    >>> reverse_str('ab')
    'ba'
    >>> reverse_str('bcb')
    'bcb'
    >>> reverse_str('0')
    '0'
    >>> reverse_str('123')
    '321'

    '''

    assert type(message) == str, 'invalid argument type'

    return message[::-1]

