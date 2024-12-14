name = input(':')
comma = name.find(',')

result = str(name[comma + 1:]).strip()

print(result)