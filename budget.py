# Simple Budget Tracker

budget = float(input("Enter total monthly budget (LKR): "))

balance = budget

while True:
    expense = input("Enter expense amount (or type 'done' to stop): ")

    if expense.lower() == "done":
        break

    expense = float(expense)
    balance = balance - expense

    print("Remaining Balance:", balance, "LKR")

    if balance < 500:
        print("Warning: Low Funds")

print("-----------------------")
print("Final Balance:", balance, "LKR")
print("-----------------------")
