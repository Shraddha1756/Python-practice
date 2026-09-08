
'''Write a python to calculate the final bill ammount after applying the discount . the program should take the total
bill amount as input from user and apply the discount accrdingto the folowing rules. after calculating the discoumt
the program should displaynthe discount amount na dthe final bill amount payble by the coustomer

Bill Amount                                          Discount
above 5000                                            20 percent
3000 to 5000                                           10 percent
Below 3000                                              no discount
'''
# solution

bill = float(input("Enter total bill amount: "))

if bill > 5000:
    discount = bill * 20/100
elif bill >= 3000:
    discount = bill * 10/100
else:
    discount = 0
final_bill = bill - discount
print("Discount amount:", discount)
print("Final bill amount:", final_bill)
