# take a password and check length, presence of @, and wheter first and last character are diffrent?

password = input("Enter password: ")

length = len(password)
has_at = "@" in password
different = password[0] != password[-1]

print("Length:", length)
print("Contains @:", has_at)
print("First and last character are different:", different)
