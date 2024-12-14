PI = 3.14159
import doctest
def circle_area(radius: float) -> float:

    '''

    Args:
        radius:

    Returns:

    >>> circle_area(2.0)
    12.56636
    >>> circle_area(4.0)
    50.26544
    '''

    assert type(radius) == float, 'invalid argument type'
    assert 0.0 <= radius <= 1000.0, 'argument out of range'



    return PI * radius ** 2

def circle_circumference(radius: float) -> float:

    '''

    Args:
        radius:

    Returns:

    >>> circle_circumference(2.0)
    12.56636
    >>> circle_circumference(4.0)
    25.13272
    '''

    assert type(radius) == float, 'invalid argument type'
    assert 0.0 <= radius <= 1000.0, 'argument out of range'

    return 2 * PI * radius

doctest.testmod()