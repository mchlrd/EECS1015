import doctest
def fruit_price(num_apples: int, num_peaches: int, num_watermelon: int) -> float:

    '''

    Args:
        num_apples:
        num_peaches:
        num_watermelon:

    Returns:

    >>> fruit_price(1, 2, 3)
    34.89
    >>> fruit_price(0, 0, 0)
    0.0
    >>> fruit_price(1.5, 2, 3)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument type
    >>> fruit_price(1, 1, 1)
    14.92
    >>> fruit_price(1, 0, 1)
    10.93
    >>> fruit_price(0, 0, 1)
    7.99
    '''

    assert type(num_apples) == int, 'invalid argument type'
    assert type(num_peaches) == int, 'invalid argument type'
    assert type(num_watermelon) == int, 'invalid argument type'

    assert num_apples >= 0, 'argument must be non-negative'
    assert num_peaches >= 0, 'argument must be non-negative'
    assert num_watermelon >= 0, 'argument must be non-negative'

    price_apples = 2.94
    price_peaches = 3.99
    price_watermelon = 7.99

    total_price = num_apples * price_apples + num_peaches * price_peaches + num_watermelon * price_watermelon

    return total_price

doctest.testmod()