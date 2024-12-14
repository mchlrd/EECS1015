from typing import List

def remove_item(data: List[str], index: int) -> List[str]:

    '''

    Args:
        data: list
        index: int at the list in time

    Returns: list of strings

    >>> remove_item(["cellphone", "laptop", "microphone"], 2)
    ['cellphone', 'laptop']
    >>> remove_item(["cellphone", "laptop", "microphone"], 0)
    ['laptop', 'microphone']

    '''

    assert 0 <= index < len(data), 'index is out of range'

    result = data[:index] + data[index+1:]

    return result

