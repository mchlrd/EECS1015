# get input
age = int(input("What is the child's age? "))
height = int(input("What is the child's height? "))

# you can add any line of code between this line and the line with return
is_eligible = not(age <= 6 and height < 120)
# show result
print(is_eligible) # You should modify this line as needed
