user_input = input('input')

comma = user_input.find(',')

first_name = user_input[comma + 1:].strip()

print(first_name)