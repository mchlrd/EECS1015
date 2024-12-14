################################### TASK 3 ###################################
### Starting code ###
import doctest


def approximate_pi(m: int) -> float:
    '''
    Approximate the value of pi using a series expansion.

    Args:
        m(int): The number of terms to use in the approximation

    Returns:
        float: An approximation of pi rounded to four decimal places.

    Examples:
        >>> approximate_pi(2)
        3.4667
        >>> approximate_pi(10)
        3.2323
        >>> approximate_pi(100)
        3.1515
        >>> approximate_pi(1000)
        3.1426
        >>> approximate_pi(0)
        4.0
    '''
    result = 0
    ### Your code here ###  

    assert type(m) == int and m >= 0, 'm must be a positive int'

    for n in range(m + 1):
        result += 4*((-1) ** n / (2 * n + 1))

    return round(result, 4)


doctest.testmod()
