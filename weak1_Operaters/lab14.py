# E-COMMERCE SYSTEM

def login():

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin":

        if password == "admin123":
            print("Login Successful")
            print("Access Level: Full Access")

        else:
            print("Incorrect Password")

    elif username == "customer":

        if password == "cust123":
            print("Login Successful")
            print("Access Level: Shopping Only")

        else:
            print("Incorrect Password")

    elif username == "cashier":

        if password == "cash123":
            print("Login Successful")
            print("Access Level: Sales and Payments")

        else:
            print("Incorrect Password")

    else:
        print("Username Not Found")


def checkout():

    subtotal = float(input("Enter subtotal: "))

    coupon = input("Enter coupon code: ")

    location = input("Location (Uganda/Kenya): ")

    discount = 0
    tax_rate = 0

    # Coupon validation
    if coupon == "SAVE10":

        if subtotal >= 100000:
            discount = subtotal * 0.10
        else:
            discount = subtotal * 0.05

    elif coupon == "SAVE20":

        if subtotal >= 200000:
            discount = subtotal * 0.20
        else:
            discount = subtotal * 0.10

    else:
        print("Invalid Coupon")
        discount = 0

    # Tax by location
    if location == "Uganda":
        tax_rate = 0.18

    elif location == "Kenya":
        tax_rate = 0.16

    else:
        tax_rate = 0.10

    amount_after_discount = subtotal - discount
    tax = amount_after_discount * tax_rate
    final_price = amount_after_discount + tax

    print("\n------ RECEIPT ------")
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final Price:", final_price)


login()
checkout()