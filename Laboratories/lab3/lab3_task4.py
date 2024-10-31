# get input
phone_number = input("Please give me your phone number: ")

# you can add any line of code between this line and the line with return
cleaned_number = phone_number.replace(' ', '').replace('-','').replace('(','').replace(')','')

result = cleaned_number.isdigit() and len(cleaned_number) == 10
# show result
print(result) # You can modify this line as needed