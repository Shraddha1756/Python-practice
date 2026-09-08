#question4: take name, branch, and year.Generate a code name using string concetation, slicin, repetition

student_name = input("Enter student name:")
branch_name = input("Enter branch:")
year = input("Enter year:")

code_name = student_name[:3] + "-" + branch_name[:3] + "-" + year[-2:]

print("*" * 30)
print("Student Code:", code_name)
print("*" * 30)
