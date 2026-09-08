'''Write a python program to create the simple password validation system
the program should repeatedly ask the user to enter a password until a valid password is entered 
a password will be consider valid only if it has at least 8 character and contain the @ symbol.

Once the user enter a valid password the password the program should display "Password accepted". and stop
otherwise , it should display " Week password". Try again." and ask for the password again.'''

while True:
    password = input("Enter password: ")

    if len(password) >= 8 and "@" in password:
        print("Password accepted")
        break
    else:
        print("Weak password. Try again.")
