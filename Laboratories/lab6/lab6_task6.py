import doctest
def remove_vowels(data: str) -> str:
    '''

    Remove all vowels from the input string.
    Args:
        data: str the input string which may contain uppercase and lowercase letters

    Returns: str the sting after removing all vowels

    Examples:

        >>> remove_vowels('bca')
        'bc'
        >>> remove_vowels('bbb')
        'bbb'
        >>> remove_vowels('heell')
        'hll'
        >>> remove_vowels('pythn')
        'pythn'
        >>> remove_vowels('  This is a fun programming exercise  ')
        '  Ths s  fn prgrmmng xrcs  '

    '''

    assert isinstance(data, str) and (data.replace(' ','').isalpha() or data == ''), 'data can only contain alphabetic characters, spaces, or be empty'
    vowels = "aeiouAEIOU"
    return ''.join([char for char in data if char not in vowels])


doctest.testmod()