def function1(value: float) -> None:
    global x
    x = value + y
    return

def function2(value: float) -> None:
    global y
    y = value
    return

def problematic_function(x_value: float, y_value: float) -> float:
    assert type(y_value) == float, "invalid argument"
    assert type(x_value) == float, 'invalid argument'

    function2(y_value)
    function1(x_value)

    y = y_value
    x = x_value + y

    # Do not modify anything below this line
    return x + y + 20


print(problematic_function(10.0, 5.0))