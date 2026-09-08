
"""
1) write the python program to determine whether a student for a scholarship.
The scholarship should be granted if the student either of the foolowing condition:
a) the student has a CGPA of 8.5 or above and attendance of 85 percent or above.
b) the student has won a national-level compedition.

the program should take cgpa, attendace percentage, and national-level compedition status as
input, then display whether the student is eligible for the scholarship?

2) Write a python program to simulate a digital lock system.

The lock should ask the user to enter a 4-digit PIN. If the entered PIN does not contain exactly 4
digit, the program should display an error mess and ask again. if the entered PIN is correct,the lock
should open. Otherwise, the program should ask the user to try again.

"""
#solution1:

cgpa = float(input("Enter Cgpa: "))
attendance = float(input("Enter attendance percentage : "))
national_winner = input("Have you wom a nation- level compledition ? yes/no: ")

if (cgpa >= 8.5 and attendance >= 85) or nationa_winner == "yes":
print("Student is eligible for scholarship.")

else:
     print ("Student is not eligible for scholarship")

