# simple_calculator.py

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def display_balance(balance):
    print(f"Current Balance: ${balance:.2f}")
