''' write a menu-driven python where the user can add item, remove, veiw cart, and exit
'''
#solution:

cart = []

while True:
    print("1.Add  2.Remove  3.View  4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        cart.append(input("Item: "))
    elif ch == 2:
        cart.remove(input("Item: "))
    elif ch == 3:
        print(cart)
    elif ch == 4:
        break
