
'''question3: take an email adress and print username,domian and reversed domain.
email = input("Enter email: ")'''

at_position = email.find("@")

username = email[:at_position]
domain = email[at_position + 1:]
reversed_domain = domain[::-1]

print("Username:", username)
print("Domain:", domain)
print("Reversed Domain:", reversed_domain)
