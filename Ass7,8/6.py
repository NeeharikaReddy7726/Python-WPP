class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew: {amount}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive!")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

def main():
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, balance)
    
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2.Withdraw")
        print("3. Display account details")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.display()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
