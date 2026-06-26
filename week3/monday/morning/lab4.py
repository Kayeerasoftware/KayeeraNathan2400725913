class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate_total_value(self):
        total = self.price * self.quantity
        print("Total Value:", total)


product1 = Product("Laptop", 2500000, 5)

print("Name:", product1.name)
print("Price:", product1.price)
print("Quantity:", product1.quantity)

product1.display_product()
product1.calculate_total_value()