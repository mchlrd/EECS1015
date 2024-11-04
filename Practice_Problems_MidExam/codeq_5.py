expression = input('Enter expression: ')

pound_symbol = expression.find('#')

x = int(expression[:pound_symbol])

y = int(expression[pound_symbol + 1:])

result = x * x - y * y

print(result)