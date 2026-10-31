# Imports
import csv
import datetime
import os


# Functions
# Add Expenses
def add_expense(expenses, category, description, amount):
    expense = {
        "date": str(datetime.date.today()),
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)


# Show Expenses
def show_expenses(expenses):
    for item in expenses:
        print(f"{item['date']} | {item['description']} | {item['category']} | £{item['amount']:.2f}")


# Total Expenses
def calculate_total(expenses):
    total = 0
    for item in expenses:
        total += item['amount']
    return total


def total_by_category(expenses, category):
    total = 0
    for item in expenses:
        if item["category"] == category:
            total += item['amount']
    return total


# Save Expenses
def save_expenses(expenses, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "description", "amount"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved.")


# Load Expenses
def load_expenses(filename):
    expenses = []
    if os.path.exists(filename):
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    else:
        print("No file could be found.")
    return expenses


# Main program
expenses = load_expenses("expenses.csv")
add_expense(expenses, "Drink", "Tea", 2.00)
show_expenses(expenses)
print(f"Total: £{calculate_total(expenses):.2f}")
save_expenses(expenses, "expenses.csv")
