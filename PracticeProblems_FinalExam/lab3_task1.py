user_input = input("Enter the expression: ")
pound_index = user_input.find('#')

x = int(user_input[:pound_index])
y = int(user_input[pound_index + 1:])

result = x*x - y*y

print(result)
