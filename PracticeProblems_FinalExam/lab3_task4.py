# get input
phone_number = input("Please give me your phone number: ")

# you can add any line of code between this line and the line with return
final_number = phone_number.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

result = final_number.isdigit() and len(final_number) == 10
# show result
print(result) # You can modify this line as needed