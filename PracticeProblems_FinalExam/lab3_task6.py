user_input = input('input')

comma = user_input.find(',')

last_name = user_input[:comma].strip()

print(last_name)
