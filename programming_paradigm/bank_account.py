# bank_account.py

class BankAccount:
    # This runs automatically when you create a new account
    def __init__(self, initial_balance=0):
        # Use __ (double underscore) to make it private
        self.__account_balance = initial_balance

    # Add money to account
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    # Withdraw money safely
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            return False  # Insufficient funds
        self.__account_balance -= amount
        return True

    # Show current balance
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance: .2f}")
