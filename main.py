# Imports
import datetime

# Lists
expenses = []

# Dictionaries
drink_expense = {
    "date": str(datetime.date.today()),
    "category": "Drink",
    "description": "Coffee",
    "amount": 3.50,
}
expenses.append(drink_expense)

food_expense = {
    "date": str(datetime.date.today()),
    "category": "Food",
    "description": "Lunch",
    "amount": 8.50,
}
expenses.append(food_expense)

travel_expense = {
    "date": str(datetime.date.today()),
    "category": "Travel",
    "description": "Train Ticket",
    "amount": 15.00,
}
expenses.append(travel_expense)

total = 0

# Display Expenses
for item in expenses:
    print(f"{item['date']} | {item['description']} | {item['category']} | £{item['amount']:.2f}")
    total += item['amount']

print(f"Total: £{total:.2f}")