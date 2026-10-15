#q3

""" ceate 
""" 
#SOL:
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

product1 = Product(name, price, quantity)

print("Product:", product1.name)
print("Total cost:", product1.calculate_total())

