import doctest

def need_to_buy_ticket(age: float, height:float) -> bool:
    '''
    Determines if a child needs to buy a ticket based on age and height.

    A child under the age of 6 (including 6) does not need to buy a ticket.
    However, if the child is taller than 120 cm (not including 120), they must
    buy a ticket regardless of their age.

    Parameters:
    - age (float): The age of the child (must be a non-negative float).
    - height (float): The height of the child in cm (must be a non-negative float).

    Returns:
    - bool: True if the child needs to buy a ticket, False otherwise.

    Examples:
    >>> need_to_buy_ticket(6,119)
    False
    >>> need_to_buy_ticket(6,121)
    True
    >>> need_to_buy_ticket(7,108)
    True
    >>> need_to_buy_ticket('6', 119)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type of age
    >>> need_to_buy_ticket(6, '119')
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type of height
    >>> need_to_buy_ticket(-2, 110)
    Traceback (most recent call last):
    ...
    AssertionError: age should be non-negative
    >>> need_to_buy_ticket(6, -28)
    Traceback (most recent call last):
    ...
    AssertionError: height should be non-negative
    >>> need_to_buy_ticket(9.5, 103.1)
    True
    >>> need_to_buy_ticket(0.4, 0.0)
    Traceback (most recent call last):
    ...
    AssertionError: height should be greater than 0
    '''

    assert isinstance(age, (int, float)), 'invalid data type of age'
    assert isinstance(height,(int, float)), 'invalid data type of height'

    assert age >= 0, 'age should be non-negative'
    assert height >= 0, 'height should be non-negative'
    assert height > 0, 'height should be greater than 0'

    buy_ticket = not(age<=6 and height<=120)

    return buy_ticket

doctest.testmod()
