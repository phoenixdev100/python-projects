import array

class BankAccount:
    def __init__(self, account_number, account_type, holder_name, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.account_type == "Savings" and amount > self.balance:
                print("Insufficient funds. Overdraft not allowed for Savings accounts.")
            elif self.account_type in ["Current", "Business"] and amount > self.balance + 10000:
                print("Overdraft limit exceeded.")
            else:
                self.balance -= amount
                self.transactions.append(f"Withdrew: {amount}")
                print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")

    def view_transactions(self):
        if self.transactions:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions found.")

# List to store all bank accounts
accounts = []

def create_account():
    acc_number = input("Enter Account Number: ")
    acc_type = input("Enter Account Type (Savings/Current/Business): ")
    holder_name = input("Enter Account Holder Name: ")
    initial_balance = int(input("Enter Initial Balance: "))
    
    if (acc_type == "Savings" and initial_balance < 1000) or (acc_type in ["Current", "Business"] and initial_balance < 5000):
        print("Initial balance is too low for the selected account type.")
        return
    
    new_account = BankAccount(acc_number, acc_type, holder_name, initial_balance)
    accounts.append(new_account)
    print("Account created successfully!")

def find_account(acc_number):
    for acc in accounts:
        if acc.account_number == acc_number:
            return acc
    return None

def admin_panel():
    while True:
        print("\nAdmin Panel")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Logout")
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            for acc in accounts:
                print(f"Account Number: {acc.account_number}, Type: {acc.account_type}, Holder: {acc.holder_name}, Balance: {acc.balance}")
        elif choice == "3":
            print("Logging out of Admin Panel...")
            break
        else:
            print("Invalid choice. Try again.")

def customer_panel():
    acc_number = input("Enter Your Account Number: ")
    account = find_account(acc_number)
    if not account:
        print("Account not found.")
        return
    
    while True:
        print("\nCustomer Panel")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Logout")
        choice = input("Enter choice: ")
        
        if choice == "1":
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.view_transactions()
        elif choice == "5":
            print("Logging out of Customer Panel...")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        print("\nWelcome to Bank Account Management System")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            admin_panel()
        elif choice == "2":
            customer_panel()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()