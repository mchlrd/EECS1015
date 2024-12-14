ALLOWED_NUMBER = 5
def calculate_average(numbers_str: str) -> float:
    '''

    Args:
        numbers_str:

    Returns:

    >>> calculate_average('1|2|3|4|5')
    3.0
    >>> calculate_average('2 | 10|  5|7|11')
    7.0
    '''

    assert type(numbers_str) == str, 'invalid argument type'

    numbers = numbers_str.split('|')

    assert len(numbers) == ALLOWED_NUMBER, 'invalid len'

    total = 0
    for num in numbers:
        total += int(num.strip())

    average = total / len(numbers)

    return average