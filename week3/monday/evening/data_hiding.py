class MobileMoney:

    def __init__(self):
        self.__balance = 0    

    def deposit(self, amount):
        self.__balance += amount
        print(f"UGX {amount:,} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"UGX {amount:,} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Current Balance: UGX {self.__balance:,}")


account = MobileMoney()


account.deposit(700000)


account.withdraw(30000)


account.check_balance()