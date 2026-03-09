# Improved Budget Tracker

budget = float(input("Enter total monthly budget (LKR): "))
balance = budget
total_expenses = 0
count = 1

print("\n--- Expense Tracker Started ---")

while True:
    expense = input(f"Enter expense #{count} (or type 'done' to stop): ")

    if expense.lower() == "done":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative.")
            continue

        balance -= expense
        total_expenses += expense

        print(f"Remaining Balance: {balance:.2f} LKR")

        if balance < 500:
            print("⚠ Warning: Low Funds")

        count += 1

    except ValueError:
        print("Invalid input. Please enter a number.")

print("\n-----------------------")
print(f"Total Budget: {budget:.2f} LKR")
print(f"Total Expenses: {total_expenses:.2f} LKR")
print(f"Final Balance: {balance:.2f} LKR")

percent_used = (total_expenses / budget) * 100
print(f"Budget Used: {percent_used:.1f}%")
print("-----------------------")

