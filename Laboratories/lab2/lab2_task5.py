weight = float(input('Weight? '))
height = float(input('Height? '))

height = height / 100
BMI = weight / (pow(height, 2))

BMI = round(BMI, 2)

print(BMI)