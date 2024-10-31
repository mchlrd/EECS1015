import doctest

PI = 3.14159

def circle_area(radius: float) -> float:
    '''
    Takes the radius r and calculates the area of the circle using A = pi*r^2

    >>> circle_area(2.0)
    12.56636
    >>> circle_area(4.0)
    50.26544
    '''
    assert type(radius) == float, "radius is not a float"
    assert 0.0 <= radius <= 1000.0, 'radius must be between 0 and 1000'

    return PI * radius ** 2

def circle_circumference(radius: float) -> float:
    '''
    Takes the radius r and calculates the circumference of the circle using C = 2*pi*r

    >>> circle_circumference(2.0)
    12.56636
    >>> circle_circumference(4.0)
    25.13272
    '''

    assert type(radius) == float, 'radius must be of a float type'
    assert 0.0 <= radius <= 1000.0, 'radius must be between 0 and 1000'

    return 2 * PI * radius

doctest.testmod()
