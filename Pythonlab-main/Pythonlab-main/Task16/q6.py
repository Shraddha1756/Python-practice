''' write apython program to store one student data as a tupple: name, roll number, and marks. display 
grade based on marks
'''
# Store student data in a tuple

student = ("Shraddha", 101, 85)


print("Name:", student[0])
print("Roll Number:", student[1])
print("Marks:", student[2])


marks = student[2]

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
