import doctest
def count_wheels(num_bicycles: int, num_tricycles: int, num_cars: int, num_trucks: int) -> int:
    '''

    Args:
        num_bicycles:
        num_tricycles:
        num_cars:
        num_trucks:

    >>> count_wheels(0, 0, 0, 0)
    0
    >>> count_wheels(1, 1, 1, 1)
    27
    >>> count_wheels(1, 0, 0, 1)
    20
    >>> count_wheels(0, 0, 0, 1)
    18

    '''

    assert type(num_bicycles) == int, 'invalid argument type'
    assert type(num_cars) == int, 'invalid argument type'
    assert type(num_trucks) == int, 'invalid argument type'
    assert type(num_tricycles) == int, 'invalid argument type'

    assert num_bicycles >= 0, 'argument must be non-negative'
    assert num_tricycles >= 0, 'argument must be non-negative'
    assert num_cars >= 0, 'argument must be non-negative'
    assert num_trucks >= 0, 'argument must be non-negative'

    result = num_bicycles * 2 + num_tricycles * 3 + num_trucks * 18 + num_cars * 4

    return result

doctest.testmod()