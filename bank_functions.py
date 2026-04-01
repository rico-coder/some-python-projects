# function for new balance after deposit
def deposit(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return balance + amount

# function for new balance after withdraw
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
