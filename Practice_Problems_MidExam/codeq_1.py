import doctest
def conversion(amount: float) -> str:
    '''
    >>> conversion(100.0)
    '135.0'
    >>> conversion(0.0)
    '0.0'
    >>> conversion(-13.5)
    Traceback (most recent call last):
    ...
    AssertionError: amount must be non-negative
    '''

    assert type(amount) == float, 'amount must be float'
    assert amount >= 0.0, 'amount must be non-negative'


    result = str(amount * 1.35)

    return result.strip()

doctest.testmod()