# get input from user
lab1_grade = int(input('Lab1? '))
lab2_grade = int(input('Lab2? '))
assignment_grade = int(input('Assignment? '))
midterm_grade = int(input('Midterm? '))
final_grade = int(input('Final? '))

# calculate the result, you can add as many lines as you need and assign the value to course_score

lab_grade = max(lab1_grade, lab2_grade)

course_score = (lab_grade * 0.05) + (assignment_grade * 0.2) + (midterm_grade * 0.25) + (final_grade * 0.5)
# show the result
print(course_score)



