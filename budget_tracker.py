import json
import os
from datetime import datetime


class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.balance = 0.0
        self.load_data()

    def add_transaction(self, amount, category, transaction_type):
        """Add a new transaction (income or expense)"""
        if transaction_type.lower() not in ['income', 'expense']:
            print("Invalid transaction type. Use 'income' or 'expense'.")
            return

        transaction = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'category': category,
            'type': transaction_type.lower()
        }

        self.transactions.append(transaction)

        if transaction_type.lower() == 'income':
            self.balance += amount
        else:
            self.balance -= amount

        self.save_data()
        print(f"Transaction added successfully! New balance: {self.balance:.2f}")

    def show_balance(self):
        """Display current balance"""
        print(f"\nCurrent Balance: {self.balance:.2f}")

    def show_transactions(self):
        """Display all transactions"""
        if not self.transactions:
            print("\nNo transactions to display.")
            return

        print("\nAll Transactions:")
        print("-" * 60)
        print("{:<20} {:<10} {:<15} {:<10}".format("Date", "Type", "Category", "Amount"))
        print("-" * 60)

        for transaction in self.transactions:
            print("{:<20} {:<10} {:<15} {:<10.2f}".format(
                transaction['date'],
                transaction['type'],
                transaction['category'],
                transaction['amount']
            ))
        print("-" * 60)
        self.show_balance()

    def save_data(self):
        """Save transactions and balance to a file"""
        data = {
            'transactions': self.transactions,
            'balance': self.balance
        }

        with open('budget_data.json', 'w') as file:
            json.dump(data, file)

    def load_data(self):
        """Load transactions and balance from a file if it exists"""
        if os.path.exists('budget_data.json'):
            try:
                with open('budget_data.json', 'r') as file:
                    data = json.load(file)
                    self.transactions = data.get('transactions', [])
                    self.balance = data.get('balance', 0.0)
            except:
                print("Error loading data. Starting with fresh budget.")
                self.transactions = []
                self.balance = 0.0


def main():
    tracker = BudgetTracker()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                amount = float(input("Enter income amount: "))
                category = input("Enter income category (e.g., Salary, Gift): ")
                tracker.add_transaction(amount, category, 'income')
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category (e.g., Food, Rent): ")
                tracker.add_transaction(amount, category, 'expense')
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '3':
            tracker.show_balance()

        elif choice == '4':
            tracker.show_transactions()

        elif choice == '5':
            print("Exiting Budget Tracker. Your data has been saved.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()