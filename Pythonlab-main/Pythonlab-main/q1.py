
#take student full name and roll no. genterate email using first 3 letterof first,name, first three letter of last 3 character o roll number
'''
question1:take student full name and roll no. genterate email using first 3 letterof first,name, 
first three letter of last 3 character o roll number

question2: take roll no. like 2024a1r057 and extract admission year, program code, and 
rollnumber digit usingslicing?

question3: take an email adress and print username,domian and reversed domain.

question4: take name, branch, and year.Generate a code name using string concetation, slicin, repetition

quesion 5 : take a password and check length, presence of @, and wheter first and last character are diffrent?

soluion:

'''
#solution1:

name = input("Enter student full name: ")
roll = input("Enter roll number: ")

parts = name.split()

first = parts[0][:3]
last = parts[-1][:3]
last3roll = roll[-3:]

email = first + last + last3roll + "@gmail.com"

print("Generated Email:", email)

#solution2:

