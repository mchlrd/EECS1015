import doctest

def count_wheels(num_bicycles: int, num_tricycles: int, num_cars: int, num_trucks: int) -> int:
    """
    Calculates the total number of wheels given the number of bicycles, tricycles, cars, and trucks.

    This function takes the number of each type of vehicle as input and calculates the total number
    of wheels they collectively have based on the following:
    - A bicycle has 2 wheels.
    - A tricycle has 3 wheels.
    - A car has 4 wheels.
    - A truck has 18 wheels.

    Parameters:
    - num_bicycles (int): Number of bicycles (must be a non-negative integer).
    - num_tricycles (int): Number of tricycles (must be a non-negative integer).
    - num_cars (int): Number of cars (must be a non-negative integer).
    - num_trucks (int): Number of trucks (must be a non-negative integer).

    Returns:
    - int: The total number of wheels for the given vehicles.

    Examples:
    >>> count_wheels(1, 0, 2, 5)
    100
    >>> count_wheels(0, 0, 0, 0)
    0
    >>> count_wheels(1.5, 2, 3, 4)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type of num_bicycles
    >>> count_wheels(1, '2', 3, 4)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type of num_tricycles
    >>> count_wheels(1, 2, -3, 4)
    Traceback (most recent call last):
    ...
    AssertionError: num_cars should be non-negative
    """
    # Assertions to validate data types and non-negative values
    assert type(num_bicycles) == int, 'invalid data type of num_bicycles'
    assert type(num_tricycles) == int, 'invalid data type of num_tricycles'
    assert type(num_cars) == int, 'invalid data type of num_cars'
    assert type(num_trucks) == int, 'invalid data type of num_trucks'

    assert num_bicycles >= 0, 'num_bicycles should be non-negative'
    assert num_tricycles >= 0, 'num_tricycles should be non-negative'
    assert num_cars >= 0, 'num_cars should be non-negative'
    assert num_trucks >= 0, 'num_trucks should be non-negative'

    # Calculate the total number of wheels
    result = num_bicycles * 2 + num_tricycles * 3 + num_cars * 4 + num_trucks * 18

    # Return the result instead of printing
    return result

doctest.testmod()
