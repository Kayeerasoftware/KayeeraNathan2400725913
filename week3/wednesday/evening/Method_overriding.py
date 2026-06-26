class BankAccount:
    def calculate_interest(self, balance,rate):
        return balance * rate/100
    def get_acount_type(self):
        return "Generic Bank Account"

class SavingsAccount(BankAccount):
    def calculate_interest(self, balance, rate):
        return balance * rate / 12 / 100
    def get_acount_type(self):
        return "Savings Account"

class CurrentAccount(BankAccount):
    def calculate_interest(self, balance, rate):
        return 0
    def get_acount_type(self):
        return "checking account"