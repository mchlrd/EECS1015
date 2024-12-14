################################### TASK 3 ###################################
### Starting code ###
import doctest
def approximate_pi(m: int) -> float:

    '''

    Args:
        m:

    Returns:

    >>> approximate_pi(2)
    3.4667
    >>> approximate_pi(3)
    2.8952
    >>> approximate_pi(4)
    3.3397
    >>> approximate_pi(9)
    3.0418
    '''

    assert type(m) == int and m >= 0, 'invalid argument type'

    result = 0  
    ### Your code here ###  
    n = 0

    while n <= m:
        result += 4 * ((-1) ** n) / (2 * n + 1)

        n+=1
    
    return round(result, 4)

doctest.testmod()