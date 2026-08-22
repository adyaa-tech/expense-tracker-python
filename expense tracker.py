import json
print("   EXPENSE TRACKER")
print("Track your expenses easily")
print()
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

expenses = load_expenses()

total_budget = 0
budget_type = ""
budget_duration = 0
budget_per_period = 0


def add_expense():
    expense_name = input("Enter expense name: ")

    while True:
        try:
            day = int(input(f"Enter day (1-{budget_duration}): "))

            if 1 <= day <= budget_duration:
                break
            else:
                print(f"Please enter a day between 1 and {budget_duration}.")

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter expense category: ")

    expenses.append({
        "day": day,
        "name": expense_name,
        "amount": amount,
        "category": category
    })

    save_expenses()

    print()
    print("Expense added successfully!")
    print("Name:", expense_name)
    print("Day:", day)
    print("Amount:", amount)
    print("Category:", category)

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    print("\nYour Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. Name: {expense['name']}, Day: {expense['day']}, "
            f"Amount: {expense['amount']}, Category: {expense['category']}"
        )

    while True:
        try:
            choice = int(input("Enter the number of the expense to delete: "))

            if 1 <= choice <= len(expenses):
                deleted_expense = expenses.pop(choice - 1)
                save_expenses()
                print("\nExpense deleted successfully!")
                print("Deleted:", deleted_expense["name"])

                break
            else:
                print("Please enter a valid number.")

        except ValueError:
            print("Please enter a valid number.")



def view_expenses():
    print("\nYour Expenses")

    for expense in expenses:
        print(
            "Name:", expense["name"],
            "| Day:", expense["day"],
            "| Amount:", expense["amount"],
            "| Category:", expense["category"]
        )


def category_summary():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nCategory-wise Expense:")

    if not category_totals:
        print("No expenses found.")
    else:
        for category, total in category_totals.items():
            print(category, ":", total)
def day_summary():
    day_totals = {}

    for expense in expenses:
        day = expense["day"]
        amount = expense["amount"]

        if day in day_totals:
            day_totals[day] += amount
        else:
            day_totals[day] = amount

    print("\nDay-wise Expense Summary:")

    if not day_totals:
        print("No expenses found.")
    else:
        for day, total in sorted(day_totals.items()):
            print("Day", day, ":", total)


def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\nTotal Expense:", total)
    print("Total Budget:", total_budget)
    print("Budget Duration:", budget_duration, "days")
    print("Budget Per Day:", budget_per_period)

    remaining = total_budget - total
    print("Remaining Budget:", remaining)

    if total <= total_budget:
        saving = total_budget - total
        print("You saved:", saving)
    else:
        overspending = total - total_budget
        print("You overspent by:", overspending)
        print("Warning: You have exceeded your budget!")


def set_budget():
    global total_budget, budget_type, budget_duration, budget_per_period

    while True:
        try:
            budget = float(input("Enter your total budget: "))

            if budget <= 0:
                print("Budget cannot be negative.")
            else:
                total_budget = budget
                break

        except ValueError:
            print("Please enter a valid number.")

    print("\nHow many days is this budget for?")
   

    

    while True:
        try:
            duration = int(input("Enter number of days: "))

            if duration > 0:
                break
            else:
                print("Number of days must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    budget_per_period = total_budget / duration
    budget_type = "days"
    budget_duration = duration

    print("Budget duration:", duration, "days")
    print("Budget per day:", budget_per_period)


set_budget()

while True:
    print("\nExpense Tracker")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Category wise Summary")
    print("5. Day wise Summary")
    print("6. Delete Expense")
    print("7. Exit")


    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        category_summary()
    elif choice == "5":
        day_summary()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        print("Thank you for using Expense Tracker")
        break

    else:
        print("Please enter a valid choice.")