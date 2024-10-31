import doctest

def pound(expression: str) -> int:
    """
    Return the result of the pound operation that is defined as "x # y" = x^2 - y^2

    Parameters:
        expression (str): The input string containing the expression with the pound operator.

    Returns:
        int: The result of the pound operation.

    Raises:
        AssertionError: If the input is invalid, such as having multiple pound signs,
                        non-integer numbers, or missing numbers.

    Examples:
    >>> pound("2 # 3")
    -5
    >>> pound(" 2 # 3")
    -5
    >>> pound("2 # 3 ")
    -5
    >>> pound("2#3")
    -5
    >>> pound("2 ##### 3")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid format: Multiple pound signs are not allowed.
    >>> pound("2 # 3 # 4 # 5")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid format: Only one pound operation is allowed.
    >>> pound("# 3")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid format: Missing numbers in the expression.
    >>> pound("2.5 # 3")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid number format: Only integers are allowed.
    >>> pound(5)
    Traceback (most recent call last):
    ...
    AssertionError: Invalid argument type.
    """

    # Check if the input is of the correct type
    assert isinstance(expression, str), "Invalid argument type."

    # Strip leading and trailing spaces
    expression = expression.strip()

    # Check for multiple pound signs
    if expression.count('#') != 1:
        raise AssertionError("Invalid format: Only one pound operation is allowed.")

    # Split the string around the pound sign
    parts = expression.split('#')

    # Check if there are exactly two parts and that they contain numeric values
    if len(parts) != 2 or not parts[0].strip() or not parts[1].strip():
        raise AssertionError("Invalid format: Missing numbers in the expression.")

    # Try converting the stripped values to integers
    try:
        x = int(parts[0].strip())
        y = int(parts[1].strip())
    except ValueError:
        raise AssertionError("Invalid number format: Only integers are allowed.")

    # Perform the pound operation: x # y = x^2 - y^2
    result = x * x - y * y

    return result

# Run the doctests
doctest.testmod()
