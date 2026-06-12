product = input("Enter product name: ")

if product == "Laptop":
    print("Laptop is available, please order")

if product == "Phone":
    print("Phone is available, please order")

if product != "Laptop" and product != "Phone":
    print("Product not available")