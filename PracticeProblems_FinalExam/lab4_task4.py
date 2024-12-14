import doctest
def need_to_buy_ticket(age: float, height: float) -> bool:
    '''

    Args:
        age:
        height:

    Returns:

    >>> need_to_buy_ticket(6,119)
    False
    >>> need_to_buy_ticket(6,121)
    True
    >>> need_to_buy_ticket(7,108)
    True
    >>> need_to_buy_ticket('6', 119)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument type
    >>> need_to_buy_ticket(6, '119')
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument type
    >>> need_to_buy_ticket(-2, 110)
    Traceback (most recent call last):
    ...
    AssertionError: age must be non-negative
    >>> need_to_buy_ticket(6, -28)
    Traceback (most recent call last):
    ...
    AssertionError: height must be non-negative
    >>> need_to_buy_ticket(9.5, 103.1)
    True
    >>> need_to_buy_ticket(0.4, 0.0)
    Traceback (most recent call last):
    ...
    AssertionError: height must be non-negative

    '''

    assert isinstance(age, (int, float)), 'invalid argument type'
    assert isinstance(height, (int, float)), 'invalid argument type'

    assert age >= 0, 'age must be non-negative'
    assert height > 0, 'height must be non-negative'

    is_eligible = not(age <= 6 and height <= 120)

    return is_eligible

doctest.testmod()