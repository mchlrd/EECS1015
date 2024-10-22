import doctest

def is_even(value: int) -> bool:
    """
    Function takes a value argument and checks if its integer part is even.

    >>> is_even(4)
    True
    >>> is_even(-5)
    False
    >>> is_even(-2)
    True
    >>> is_even(5)
    False
    """
    assert type(value) == int, 'invalid argument'
    return value % 2 == 0

if __name__ == "__main__":
    doctest.testmod()