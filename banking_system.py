# banking_system.py

from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account = Account()
        self.accounts[account.account_number] = account

    def deposit(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            balance = self.accounts[account_number].balance
            print(f"Account Balance: {balance}")
        else:
            print("Account not found.")
