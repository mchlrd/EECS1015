user_input = input('Enter the input: ')

pound_symbol = user_input.find('#')

x = int(user_input[:pound_symbol])

y = int(user_input[pound_symbol + 1:])

result = x * x - y * y

print(result)
