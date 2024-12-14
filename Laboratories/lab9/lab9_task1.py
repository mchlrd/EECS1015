ALLOWED_NUMBER = 5
def calculate_average(numbers_str: str) -> float:

    '''


    Args:
        numbers_str: A string containing 5 numbers separated by '|'

    Returns: The average of numbers

    >>> calculate_average('1|2|3|4|5')
    3.0
    >>> calculate_average('2 | 10|  5|7|11')
    7.0

    '''

    assert type(numbers_str) == str, 'Invalid input type'

    numbers = numbers_str.split('|')

    assert len(numbers) == ALLOWED_NUMBER, 'Input must contain exactly 5 numbers'

    total = 0
    total += int(numbers[0].strip())
    total += int(numbers[1].strip())
    total += int(numbers[2].strip())
    total += int(numbers[3].strip())
    total += int(numbers[4].strip())

    average = total / len(numbers)

    return average