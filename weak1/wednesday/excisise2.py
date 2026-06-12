print("=" * 60)
print("        NATHAN ONLINE SHOP - ONLINE STORE")
print("=" * 60)

# LOGIN SYSTEM

username = input("Username: ")
password = input("Password: ")

logged_in = False
role = ""

if username == "admin" and password == "admin123":
    logged_in = True
    role = "Admin"

elif username == "customer" and password == "cust123":
    logged_in = True
    role = "Customer"

elif username == "cashier" and password == "cash123":
    logged_in = True
    role = "Cashier"


# PRODUCT DATABASE (CATALOGUE)

products = {
    1: {"name": "Smartphone", "price": 800000},
    2: {"name": "Laptop", "price": 1500000},
    3: {"name": "Headphones", "price": 120000},
    4: {"name": "Smart Watch", "price": 250000}
}

# IF LOGIN SUCCESSFUL

if logged_in:

    print("\nLogin Successful!")
    print("Welcome,", role)

    # Role permissions
    if role == "Admin":
        print("Access: Full system control (users, products, reports)")
    elif role == "Cashier":
        print("Access: Process sales and payments")
    else:
        print("Access: Browse and purchase products")

    # PRODUCT BROWSING

    print("\n" + "=" * 60)
    print("            AVAILABLE PRODUCTS")
    print("=" * 60)

    for key in products:
        print(f"{key}. {products[key]['name']} - UGX {products[key]['price']:,.0f}")

    print("=" * 60)

    # CUSTOMER SELECTS PRODUCT

    choice = int(input("Select product number: "))

    if choice in products:
        selected_product = products[choice]

        quantity = int(input("Enter quantity: "))

        subtotal = selected_product["price"] * quantity

        print(f"\nSelected: {selected_product['name']}")
        print(f"Subtotal: UGX {subtotal:,.0f}")

        # DISCOUNT RULES
  
        if subtotal >= 500000:
            discount_rate = 15
        elif subtotal >= 200000:
            discount_rate = 10
        elif subtotal >= 100000:
            discount_rate = 5
        else:
            discount_rate = 0

        discount_amount = subtotal * discount_rate / 100



        # COUPON SYSTEM

        coupon = input("\nEnter coupon code: ")

        coupon_rate = 0

        if coupon == "SAVE10":
            coupon_rate = 10
            print("Coupon applied: SAVE10 (10%)")
        elif coupon == "SAVE20":
            coupon_rate = 20
            print("Coupon applied: SAVE20 (20%)")
        elif coupon == "":
            print("No coupon applied")
        else:
            print("Invalid coupon code")

        after_discount = subtotal - discount_amount
        coupon_amount = after_discount * coupon_rate / 100
        after_coupon = after_discount - coupon_amount


        # TAX SYSTEM

        print("\nChoose Location:")
        print("1. Kampala")
        print("2. Wakiso")
        print("3. Mukono")
        print("4. Other")

        location = input("Location: ")

        if location.lower() == "kampala":
            tax = 18
        elif location.lower() == "wakiso":
            tax = 15
        elif location.lower() == "mukono":
            tax = 12
        else:
            tax = 10

        tax_amount = after_coupon * tax / 100
        final_price = after_coupon + tax_amount


        # RECEIPT

        print("\n" + "=" * 60)
        print("                 RECEIPT")
        print("=" * 60)

        print(f"Product        : {selected_product['name']}")
        print(f"Quantity       : {quantity}")
        print(f"Unit Price     : UGX {selected_product['price']:,.0f}")
        print(f"Subtotal       : UGX {subtotal:,.0f}")
        print(f"Discount       : {discount_rate}% = UGX {discount_amount:,.0f}")
        print(f"Coupon         : {coupon_rate}% = UGX {coupon_amount:,.0f}")
        print(f"Tax            : {tax}% = UGX {tax_amount:,.0f}")

        print("-" * 60)
        print(f"FINAL PRICE    : UGX {final_price:,.0f}")
        print("=" * 60)

    else:
        print("Invalid product selection!")

else:
    print("\nLogin Failed! Invalid credentials.")