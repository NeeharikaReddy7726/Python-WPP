class Customer:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display(self):
        print(f"Customer: {self.name}, Account Number: {self.account_number}, Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists")
        else:
            self.customers[account_number] = Customer(name, account_number, initial_balance)
            print(f"Customer {name} added with account number {account_number}")

    def remove_customer(self, account_number):
        if account_number not in self.customers:
            print("Account number not found")
        else:
            del self.customers[account_number]
            print(f"Customer with account number {account_number} removed")

    def get_customer(self, account_number):
        if account_number in self.customers:
            return self.customers[account_number]
        else:
            print("Account number not found")
            return None

    def display_all_customers(self):
        if not self.customers:
            print("No customers in the bank")
        else:
            for customer in self.customers.values():
                customer.display()


# Taking input from the user
bank = Bank()
while True:
    action = input("Choose an action (add, remove, deposit, withdraw, display, display_all, exit): ").strip().lower()
    if action == "add":
        name = input("Enter customer name: ").strip()
        account_number = input("Enter account number: ").strip()
        initial_balance = float(input("Enter initial balance: ").strip())
        bank.add_customer(name, account_number, initial_balance)
    elif action == "remove":
        account_number = input("Enter account number to remove: ").strip()
        bank.remove_customer(account_number)
    elif action == "deposit":
        account_number = input("Enter account number: ").strip()
        amount = float(input("Enter amount to deposit: ").strip())
        customer = bank.get_customer(account_number)
        if customer:
            customer.deposit(amount)
    elif action == "withdraw":
        account_number = input("Enter account number: ").strip()
        amount = float(input("Enter amount to withdraw: ").strip())
        customer = bank.get_customer(account_number)
        if customer:
            customer.withdraw(amount)
    elif action == "display":
        account_number = input("Enter account number: ").strip()
        customer = bank.get_customer(account_number)
        if customer:
            customer.display()
    elif action == "display_all":
        bank.display_all_customers()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please choose 'add', 'remove', 'deposit', 'withdraw', 'display', 'display_all', or 'exit'.")
