''' write a pp to store all months name as tuple, input a month number and 
display the coressponding month name.
'''

months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

n = int(input("Enter month number (1-12): "))

print("Month is:", months[n-1])
