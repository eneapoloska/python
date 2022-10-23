from bank_account import BankAccount
class User:

    def __init__(self,name):
        self.name=name
        self.account={
            "checking": BankAccount(0.01),
            "savings": BankAccount(0.)
        }

    def print_balance(self):
        print(f"The saving account balnace is {self.account['savings'].balance} and the checking account is {self.account['checking'].balance}")

user1=User("Enea")
user1.account["savings"].deposit(100).display_account_info()
user1.account["savings"].withdraw(30).display_account_info()
user1.print_balance()