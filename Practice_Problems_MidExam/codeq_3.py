def formatting(word: str) -> str:

    '''
    >>> formatting("print(34)")
    'return 34'
    >>> formatting("print(0)")
    'return 0'
    >>> formatting("print(24357987862)")
    'return 24357987862
    >>> formatting("print(2)")
    'return 2'
    >>> formatting("print(-875)")
    'return -875'
    >>> formatting(" print(75) ")
    'return 75'
    >>> formatting("print(variable_a)")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid parameter
    >>> formatting("prin(27)")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid syntax
    >>> formatting("print27)")
    Traceback (most recent call last):
    ...
    Assertion Error: Invalid syntax
    '''

    assert word.startswith('python(') and word.endswith(')'), 'Invalid syntax'
    assert number_str.lstrip('-').isdigit(), 'Invalid parameter'

    word = word.strip()

    number_str = word[6:-1]

    return f'return {number_str}'