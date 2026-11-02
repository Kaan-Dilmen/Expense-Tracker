# Imports
import csv
import datetime
import os

import pandas as pd

import reports


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
        print(
            f"{item['date']} | {item['description']} | {item['category']} | £{item['amount']:.2f}"
        )


# Total Expenses
def calculate_total(expenses):
    total = 0
    for item in expenses:
        total += item["amount"]
    return total


def total_by_category(expenses, category):
    total = 0
    for item in expenses:
        if item["category"] == category:
            total += item["amount"]
    return total


# Save Expenses
def save_expenses(expenses, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["date", "category", "description", "amount"]
        )
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


# Show Menu
def show_menu():
    print("1. Add expense")
    print("2. View expenses")
    print("3. View Totals")
    print("4. Quit")
    print("5. View Reports")


# Ask for Amount
def ask_for_amount():
    while True:
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if amount <= 0:
            print("Amount must be more than zero.")
            continue
        return amount


# Show Reports
def show_reports(expenses):
    if not expenses:
        print("No expenses to report.")
        return
    df = pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["date"])
    print("Category Totals:")
    print(reports.category_totals(df))
    print("\nMonthly Totals:")
    print(reports.monthly_totals(df))
    print("\nBiggest Expense:")
    print(reports.biggest_expense(df))


# Main program
def main():
    expenses = load_expenses("expenses.csv")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Category: ")
            description = input("Description: ")
            amount = ask_for_amount()
            add_expense(expenses, category, description, amount)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print(f"Total: £{calculate_total(expenses):.2f}")
        elif choice == "4":
            save_expenses(expenses, "expenses.csv")
            break
        elif choice == "5":
            show_reports(expenses)
        else:
            print("Please choose 1-5")


main()
