from typing import List
import doctest
def intersecting_chars(my_str: str) -> List[str]:
    '''

    Args:
        my_str:

    Returns:

    >>> intersecting_chars("ab_ab_bCC")
    ['b']
    >>> intersecting_chars("abc_abc_abc")
    ['a', 'b', 'c']
    >>> intersecting_chars("ab_b_b")
    ['b']
    >>> intersecting_chars("_a_a")
    []
    '''

    assert type(my_str) == str, 'invalid argument type'
    assert my_str.count('_') == 2, 'invalid input'
    assert all(char.isalpha() or char == '_' for char in my_str), 'must contain only letters'

    parts = my_str.lower().split('_')

    sets = [set(part) for part in parts]

    intersection = set.intersection(*sets)

    return sorted(intersection)

doctest.testmod()