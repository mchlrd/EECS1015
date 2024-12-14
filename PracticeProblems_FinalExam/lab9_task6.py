from typing import List
def remove_item(data: List[str], index: int) -> List[str]:
    '''

    Args:
        data:
        index:

    Returns:

    '''

    assert 0 <= index < len(data), 'index out of range'

    result = data[:index] + data[index + 1:]

    return result