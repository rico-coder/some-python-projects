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

# function for information
def get_summary(owner,**kwargs):
    print(f"\nAccount Summary for {owner}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# function for choice
def pick_choice(choice, balance):
    match choice:
        case "1":
            amount = int(input("Deposit amount: "))
            return deposit(balance, amount)
        case "2":
            amount = int(input("Withdraw amount: "))
            return withdraw(balance, amount)
        case "3":
            return balance
        case "4":
            return None
        case _:
            print("Invalid choice.")
            return balance
