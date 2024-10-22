import doctest
import re

def absolute_value(value: str) -> float:
    """
    Extracts the number from a string formatted with | symbols and returns the absolute value as a float.
    
    :param value: A string representing a number enclosed in | symbols.
    :return: The absolute value of the number as a float.
    
    Examples:
    >>> absolute_value("|2.3|")
    2.3
    >>> absolute_value("|-3|")
    3.0
    >>> absolute_value("|0|")
    0.0
    >>> absolute_value("|123.45|")
    123.45
    >>> absolute_value('|     17.7       |')
    17.7
    >>> absolute_value('|217|')
    217.0
    >>> absolute_value('|-8.88|')
    8.88
    >>> absolute_value('|70.8|31.475|')
    Traceback (most recent call last):
        ...
    AssertionError: invalid format
    >>> absolute_value('   |-28.06|      ')
    28.06
    >>> absolute_value('|-3657-87|')
    Traceback (most recent call last):
        ...
    AssertionError: invalid format
    >>> absolute_value('|3657-87|')
    Traceback (most recent call last):
        ...
    AssertionError: invalid format
    >>> absolute_value('|51.0.33|')
    Traceback (most recent call last):
        ...
    AssertionError: invalid format
    >>> absolute_value('|abc36@|')
    Traceback (most recent call last):
        ...
    AssertionError: invalid format
    >>> absolute_value('|365787-|')
    Traceback (most recent call last):
        ...
    AssertionError: invalid format
    >>> absolute_value('||')
    Traceback (most recent call last):
        ...
    AssertionError: invalid format
    >>> absolute_value('   |92.0966|          ')
    92.0966
    >>> absolute_value('        |35.7| ')
    35.7
    """
    assert type(value) == str, 'invalid argument'
    
    value = value.strip()
    start = value.find('|')
    end = value.rfind('|')
    
    assert start != -1 and end != -1 and start != end, 'invalid format'
    
    number_str = value[start+1:end].strip()
    if not re.fullmatch(r'-?\d+(\.\d+)?', number_str):
        raise AssertionError('invalid format')
    
    number = float(number_str)
    
    return abs(number)

if __name__ == "__main__":
    doctest.testmod()
