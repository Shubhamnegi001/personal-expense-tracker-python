# ================================
# PERSONAL EXPENSE TRACKER
# ================================

from datetime import datetime

expenses = {}   # {date: [ {Category, Amount}, ... ] }

# -------------------------------
# Add Expense
# -------------------------------

def add_expense():
    try:
        user_date = input("Enter date (DD/MM/YYYY) : ")
        date_obj = datetime.strptime(user_date, "%d/%m/%Y")

        category = input("Enter Category : ").upper()
        amount = float(input("Enter Amount : "))

        if amount <= 0:
            print("Amount should be positive..")
            return

        if date_obj not in expenses:
            expenses[date_obj] = []

        expenses[date_obj].append({
            "Category": category,
            "Amount": amount
        })

        print("Expense Added Successfully..")

    except ValueError:
        print("Invalid Input..")


# -------------------------------
# View Expenses
# -------------------------------

def view_expense():
    if not expenses:
        print("No Data Found..")
        return

    print("\n================== EXPENSES ==================")
    print("-" * 60)
    print(f"{'Date':<15}{'Category':<20}{'Amount':<15}")
    print("-" * 60)

    for date, items in sorted(expenses.items()):
        for exp in items:
            print(
                f"{date.strftime('%d/%m/%Y'):<15}"
                f"{exp['Category']:<20}"
                f"{exp['Amount']:<15}"
            )

    print("-" * 60)


# -------------------------------
# Search By Category
# -------------------------------

def search_by_category():
    if not expenses:
        print("No record Found..")
        return

    search_cat = input("Enter Category : ").upper()
    found = False
    total = 0

    print("\n=========== FILTERED EXPENSES ===========")
    print("-" * 60)
    print(f"{'Date':<15}{'Category':<20}{'Amount':<15}")
    print("-" * 60)

    for date, items in expenses.items():
        for exp in items:
            if exp["Category"] == search_cat:
                print(
                    f"{date.strftime('%d/%m/%Y'):<15}"
                    f"{exp['Category']:<20}"
                    f"{exp['Amount']:<15}"
                )
                total += exp["Amount"]
                found = True

    if found:
        print("-" * 60)
        print(f"{search_cat} TOTAL : {total}")
    else:
        print("Category Not Found..")


# -------------------------------
# Total Spending
# -------------------------------

def total_spending():
    if not expenses:
        print("No Record Found..")
        return

    total = 0
    for items in expenses.values():
        for exp in items:
            total += exp["Amount"]

    print("Total Spending :", round(total, 2))


# -------------------------------
# Highest Expense
# -------------------------------

def highest_expense():
    if not expenses:
        print("No Record Found..")
        return

    highest = None

    for items in expenses.values():
        for exp in items:
            if highest is None or exp["Amount"] > highest["Amount"]:
                highest = exp

    print("\n========== HIGHEST EXPENSE ==========")
    print("Category :", highest["Category"])
    print("Amount   :", highest["Amount"])


# -------------------------------
# Average Expense
# -------------------------------

def average_expense():
    if not expenses:
        print("No Records Found..")
        return

    total = 0
    count = 0

    for items in expenses.values():
        for exp in items:
            total += exp["Amount"]
            count += 1

    avg = total / count
    print("Average Expense :", round(avg, 2))


# -------------------------------
# Save To File
# -------------------------------

def save_file():
    with open("expenses.txt", "w") as file:
        for date, items in expenses.items():
            for exp in items:
                file.write(
                    f"{date.strftime('%d/%m/%Y')},"
                    f"{exp['Category']},"
                    f"{exp['Amount']}\n"
                )

    print("Data saved to expenses.txt")


# -------------------------------
# MAIN MENU
# -------------------------------

while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Category Expense")
    print("4. Total Spending")
    print("5. Highest Expense")
    print("6. Average Expense")
    print("7. Save To File")
    print("8. Exit")

    try:
        choice = int(input("Enter Choice (1-8): "))
    except ValueError:
        print("Enter numbers only!")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        search_by_category()
    elif choice == 4:
        total_spending()
    elif choice == 5:
        highest_expense()
    elif choice == 6:
        average_expense()
    elif choice == 7:
        save_file()
    elif choice == 8:
        print("Thanks For Using Expense Tracker 👍")
        break
    else:
        print("Invalid Choice..")