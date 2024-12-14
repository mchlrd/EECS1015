# get input
# type 1 for True, press enter without input any value is False
a = bool(input("a = "))
b = bool(input("b = "))
    
# do the calculation
# The result is True iff it is not both True and both False

result = (a or b) and not (a and b)

print(result)