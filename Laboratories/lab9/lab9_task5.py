from typing import List
def remove_item(data: List[str], removable: str) -> List[str]:
    '''

    Args:
        data: list
        removable: string

    Returns: list without removable

    >>> remove_item(["cellphone", "laptop", "microphone"], "cellphone")
    ['laptop', 'microphone']
    >>> remove_item(["cellphone", "laptop", "microphone"], 'microphone')
    ['cellphone', 'laptop']

    '''

    assert type(data) == list, 'invalid input type'
    assert type(removable) == str, 'invalid input type'

    result = []

    for item in data:
        if item != removable:

            result.append(item)

    return result

