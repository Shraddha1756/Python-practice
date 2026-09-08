question1:take student full name and roll no. genterate email using first 3 letterof first,name, 
first three letter of last 3 character o roll number

#solution1:

name = input("Enter student full name: ")
roll = input("Enter roll number: ")

parts = name.split()

first = parts[0][:3]
last = parts[-1][:3]
last3roll = roll[-3:]

email = first + last + last3roll + "@gmail.com"

print("Generated Email:", email)
