"""
Description: This script create a class to handle account
Author: Dhruval patel
"""

class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def deposit (self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdraw.")
        else:
            print("Insufficient balance or invalid amount.")
    def get_balance(self):
        return self.__balance

# Create an account object    
account = Account("James", 100)             

# Accessing public attribute
print(account.owner)                          # Output : James

# Accessing private attribute (will raise an AttriuteError)
# print(account.__balance)

# Using public methods to interact with private data 
account.deposit(50)                 # output : $50 deposited.
print(account.get_balance())        # output : 150
account.withdraw(75)                # output : $75 withdrawn.
print(account.get_balance())        # output : 75