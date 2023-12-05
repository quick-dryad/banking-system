# account.py

import random

class Account:
    def __init__(self):
        self.account_number = self.generate_account_number()
        self.balance = 0

    def generate_account_number(self):
        return str(random.randint(10000, 99999))

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds.")
