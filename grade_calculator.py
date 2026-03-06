# Continuous Grade Calculator with Formatted Output

while True:
    print("\n" + "="*30)
    name = input("Enter Student Name (or 'Exit'): ")

    if name.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break

    try:
        # Collecting marks
        s1 = float(input("Subject 1: "))
        s2 = float(input("Subject 2: "))
        s3 = float(input("Subject 3: "))

        average = (s1 + s2 + s3) / 3

        # Determine Grade
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # --- Clean Formatted Output ---
        print("-" * 30)
        print(f"Name    : {name}")
        print(f"Average : {average:.1f}")
        print(f"Grade   : {grade}")
        print("-" * 30)

    except ValueError:
        print("Error: Please enter numbers for the marks.")