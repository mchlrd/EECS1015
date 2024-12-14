from typing import List
import doctest

def remove_item(data: List[str], product: str) -> List[str]:
    '''
    
    Args:
        data:
        product:

    Returns:

    '''
    assert type(data) == list, 'invalid argument type'
    assert type(product) == str, 'invalid argument type'

    result = []

    for item in data:
        if item != product:
            result.append(item)
        else:
            pass

    return result