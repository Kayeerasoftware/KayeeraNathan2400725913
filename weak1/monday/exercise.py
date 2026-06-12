# Uganda Bill Split Calculator

print("=" * 60)
print("     WANDEGEYA RESTAURANT BILL SPLIT CALCULATOR")
print("=" * 60)

# Getting bill amount
while True:
    try:
        bill_amount = float(input("Enter total restaurant bill (UGX): "))
        if bill_amount <= 0:
            print("Bill amount must be greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid amount.")

# Getting the number of people
while True:
    try:
        people = int(input("How many friends are sharing the bill? "))
        if people <= 0:
            print("Number of people must be at least 1.")
        else:
            break
    except ValueError:
        print("Please enter a valid whole number.")

# Tip options
print("\nChoose a service tip from the list below:")
print("1. 10% (Good Service)")
print("2. 15% (Very Good Service)")
print("3. 20% (Excellent Service)")
print("4. Custom Tip")

while True:
    choice = input("Select option (1-4): ")

    if choice == "1":
        tip_percent = 10
        break
    elif choice == "2":
        tip_percent = 15
        break
    elif choice == "3":
        tip_percent = 20
        break
    elif choice == "4":
        while True:
            try:
                tip_percent = float(input("Enter custom tip percentage: "))
                if tip_percent < 0:
                    print("Tip percentage cannot be negative.")
                else:
                    break
            except ValueError:
                print("Enter a valid number.")
        break
    else:
        print("Invalid choice. Please select 1-4.")

# Calculations
tip_amount = bill_amount * (tip_percent / 100)
total_bill = bill_amount + tip_amount
share_per_person = total_bill / people

# Receipt
print("\n" + "=" * 60)
print("          WANDEGEYA RESTAURANT RECEIPT")
print("=" * 60)
print(f"Restaurant Bill      : UGX {bill_amount:,.0f}")
print(f"Service Tip          : {tip_percent}%")
print(f"Tip Amount           : UGX {tip_amount:,.0f}")
print("-" * 60)
print(f"Total Amount         : UGX {total_bill:,.0f}")
print(f"People Sharing Bill  : {people}")
print("-" * 60)
print(f"Each Person Pays     : UGX {share_per_person:,.0f}")
print("=" * 60)
print("Webale nnyo! Thank you for using the calculator.")
print("=" * 60)