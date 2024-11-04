# get input
# type 1 for True, press enter without input any value is False
a = bool(input("a = "))
b = bool(input("b = "))
    
# do the calculation
# The result is True iff it is not both True and both False
is_both_true = a or b
is_both_false = a and b

result = (not(a and b)) or (not(a or b))

# show the result
print(result)