'''write a python program to input a number and check whether it is prime or not . a number is prime if it 
has no divisor other than 1 and itself'''

#solution:

number = int (input("Enter the number:"))
is_prime=True
if number <= 1:
 is_prime=True
else:
 for i in range(2, number):
 if num%i == 0:
  is is_prime= False
break

 if is_prime:
 print("Prime")
else: 
print("Not prime")
 
