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

# Main program
name = input("Please enter your name: ")
age = input("Please enter your age: ")
balance = 0

while True:
    print("\nSelect action:")
    print("1: Deposit")
    print("2: Withdraw")
    print("3: User Information")
    print("4: Exit")

    choice = input()

    if choice == "3":
        get_summary(name, age=age, balace=balance)
        continue

    balance_or_none = pick_choice(choice, balance)

    if balance_or_none is None:
        print("Goodbye!")
        break

    balance = balance_or_none
    print(f"New balance: {balance}")
