def count_primes(start: int, stop: int) -> int:
    '''

    Args:
        start:
        stop:

    Returns:

    >>> count_primes(3, 10)
    3
    >>> count_primes(2, 12)
    5
    >>> count_primes(1, 100)
    25
    '''

    assert type(start) == int and start > 0, 'invalid argument type'
    assert type(stop) == int and start > 0, 'invalid argument type'

    counter = 0

    for i in range(start, stop + 1):
        if is_prime(i):
            counter += 1

    return counter


def is_prime(num: int) -> bool:
    '''

    Args:
        num:

    Returns:

    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    >>> is_prime(23)
    True
    '''

    assert type(num) == int and num > 0, 'invalid argument type'

    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True