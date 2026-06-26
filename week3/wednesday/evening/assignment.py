
class Transaction:

    def __init__(self, employee_name, balance):
        self.employee_name = employee_name
        self.balance = balance

    def process(self, amount=0, recipient=None):
        print("Transaction Processing...")

    def display_balance(self):
        print(f"Current Balance: UGX {self.balance:,.0f}")


class Deposit(Transaction):

    def process(self, amount=0, recipient=None):
        self.balance += amount

        print("\n" + "=" * 50)
        print("DEPOSIT TRANSACTION")
        print("=" * 50)
        print(f"Employee Name : {self.employee_name}")
        print(f"Amount Deposited : UGX {amount:,.0f}")

        self.display_balance()

class Withdraw(Transaction):

    def process(self, amount=0, recipient=None):

        print("\n" + "=" * 50)
        print("WITHDRAW TRANSACTION")
        print("=" * 50)

        if amount > self.balance:
            print("Transaction Failed!")
            print("Reason: Insufficient Funds")
        else:
            self.balance -= amount

            print(f"Employee Name : {self.employee_name}")
            print(f"Amount Withdrawn : UGX {amount:,.0f}")

            self.display_balance()

class Transfer(Transaction):

    def process(self, amount=0, recipient=None):

        print("\n" + "=" * 50)
        print("TRANSFER TRANSACTION")
        print("=" * 50)

        if amount > self.balance:
            print("Transaction Failed!")
            print("Reason: Insufficient Funds")

        else:
            self.balance -= amount

            print(f"Employee Name : {self.employee_name}")
            print(f"Recipient : {recipient}")
            print(f"Amount Transferred : UGX {amount:,.0f}")

            self.display_balance()


print("=" * 60)
print("      EMPLOYEE BANKING MANAGEMENT SYSTEM")
print("=" * 60)

employee_name = "Nathan"

opening_balance = 1_000_000

print(f"\nEmployee Name : {employee_name}")
print(f"Opening Balance : UGX {opening_balance:,.0f}")

deposit = Deposit(employee_name, opening_balance)
deposit.process(500000)

withdraw = Withdraw(employee_name, deposit.balance)
withdraw.process(200000)

transfer = Transfer(employee_name, withdraw.balance)

# Method Overloading
transfer.process(100000, "Sarah")


print("\n" + "=" * 60)
print("FINAL ACCOUNT SUMMARY")
print("=" * 60)

print(f"Employee Name : {employee_name}")
print(f"Final Balance : UGX {transfer.balance:,.0f}")

print("\nThank you for using the Banking System.")