import os
import json

# Function to get user input for daily expenses
def get_expense_input():
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (food, transportation, entertainment): ")
    return {"amount": amount, "description": description, "category": category}

#store expense data
def store_expense_data(expense_data):
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    else:
        expenses = []
    expenses.append(expense_data)
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

#expenses
def categorize_expenses(expenses):
    categories = {"food": 0, "transportation": 0, "entertainment": 0}
    for expense in expenses:
        categories[expense["category"]] += expense["amount"]
    return categories

#user spending patterns
def analyze_spending(categories):
    print("\nMonthly Summary:")
    total_spending = sum(categories.values())
    print(f"Total amount spent: ${total_spending}")
    for category, amount in categories.items():
        print(f"{category}: ${amount}")

#User Interface
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Analyze Spending")
    print("3. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        expense_data = get_expense_input()
        store_expense_data(expense_data)
    elif choice == 2:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        categories = categorize_expenses(expenses)
        analyze_spending(categories)
    elif choice == 3:
        print("Thank you for using the Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
    