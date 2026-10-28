# Imports
import datetime

# Lists
expenses = []

# Functions
def add_expense(expenses, category, description, amount):
    expense = {
        "date": str(datetime.date.today()),
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)

# Add Expenses
add_expense(expenses, "Drink", "Coffee", 3.50)
add_expense(expenses, "Food", "Lunch", 8.50)
add_expense(expenses, "Travel", "Train Ticket", 15.00)

def show_expenses(expenses):
    for item in expenses:
        print(f"{item['date']} | {item['description']} | {item['category']} | £{item['amount']:.2f}")
    
# Show Expenses
show_expenses(expenses)

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

# Return Total
print(f"Food: £{total_by_category(expenses, 'Food'):.2f}")
print(f"Drink: £{total_by_category(expenses, 'Drink'):.2f}")
print(f"Travel: £{total_by_category(expenses, 'Travel'):.2f}")
print(f"Total: £{calculate_total(expenses):.2f}")