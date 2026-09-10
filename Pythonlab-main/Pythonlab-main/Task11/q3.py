'''write a python program that ask the user to enter a username and password. the user should 
get 3 attempt. if the correct credentails and entered , display "Login sucessfully" and stop 
the loop. if all attempt are used , display "Account Locked"
'''
#solution:
username = "admin"
password = "12345"
attempt = 3
while attempt > 0:
    user = input("Enter username: ")
    pas = input("Enter password: ")

    if user == username and pas == password:
        print("Login successfully")
        break
    else:
        attempt = attempt - 1
        print("Wrong username or password")
if attempt == 0:
    print("Account Locked")
