weight = float(input('Weight: '))
height = float(input('Height (cm): '))

height_updated = height/100

BMI = round((weight/height_updated**2), 2)


print(BMI)