class BankAccount:
    def __init__(self, int_rate):
        self.int_rate = int_rate
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance -amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self

    def display_account_info(self):
        print("Your balance is", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.print_all_accounts:
            account.displapy_account_info()

first_account=BankAccount (0.08)
first_account.display_account_info().deposit(300).display_account_info().deposit(100).display_account_info().deposit(250).display_account_info().withdraw(400).display_account_info().yield_interest().display_account_info()

second_account=BankAccount (0.05)
second_account.display_account_info().deposit(200).display_account_info().deposit(100).display_account_info().withdraw(80).display_account_info().withdraw(100).display_account_info().withdraw(110).display_account_info().withdraw(100).yield_interest().display_account_info()
