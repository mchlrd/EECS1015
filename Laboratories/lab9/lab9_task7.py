from typing import Tuple

def remove_item(data: Tuple[str], index: int) -> Tuple[str]:
    '''
    Args:
        data (Tuple[str, ...]): Tuple of product names.
        index (int): Index of the product to remove.

    Returns:
        Tuple[str, ...]: New tuple with the specified item removed.

    Examples:
        >>> remove_item(("cellphone", "laptop", "microphone"), 2)
        ('cellphone', 'laptop')
        >>> remove_item(("cellphone", "pineapple", "microphone"), 1)
        ('cellphone', 'microphone')
        >>> remove_item(("apple", "banana", "cherry", "date"), 0)
        ('banana', 'cherry', 'date')
        >>> remove_item(("apple", "banana", "cherry", "date"), 3)
        ('apple', 'banana', 'cherry')
    '''

    assert 0 <= index < len(data), 'index is out of range'

    result = data[:index] + data[index + 1:]

    return result
