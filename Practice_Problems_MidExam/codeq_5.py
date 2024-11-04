def right_justify(s):
    columnCount = 70-len(s)
    whites = ' '*columnCount
    return whites + s

print(right_justify('monty'))