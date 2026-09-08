""" write a python proram to input marks of 5 student :
For each student the program should check wether the enetred marks are valid or invalid.Marks are considered
valid only if they are btw 0 and 100.if the marks are invalid the program should display "Invalid marks skipped
and move to the next student without printing those marks.

if the marks are valid ,the program should display the marks are valid.
"""
for i in range(5):
    marks= float(input("Enter marks: "))
    if marks < 0  or marks > 100:
        print("Invalid Marks")
        continue
    else:
        print("Marks are valid")
