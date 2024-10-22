user_input = input('Enter the input: ')

comma = user_input.find(',')

first_name = str(user_input[comma + 1:]).strip()

print(first_name)