class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False


def display_menu():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    account = Account()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Balance: ${account.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            if account.deposit(amount):
                print("Deposit successful.")
            else:
                print("Invalid deposit amount.")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            if account.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Invalid withdrawal amount or insufficient balance.")
        elif choice == '4':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()