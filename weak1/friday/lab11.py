# fruits = ["Mango", "Apple", "Banana", "Orange", "Pineapple"]

# for fruit in fruits:
#     print(fruit)

# count =1 
# while count <=5:
# print(count)
# count += 1


balance = 15000000

while balance > 0:
    print(f"Balance: UGX{balance:.2f}")
    action = input("Deposit or withdraw? (d/w): ").lower()
    amount = float(input("Amount: UGX"))
    
    if action == "d":
        balance += amount
    elif action == "w":
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds.")

print("Balance is UGX0.00. Program ended.")
