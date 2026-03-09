# Improved Continuous Grade Calculator

student_count = 0
total_class_average = 0

while True:
    print("\n" + "=" * 30)
    name = input("Enter Student Name (or 'exit'): ")

    if name.lower() == "exit":
        break

    try:
        s1 = float(input("Subject 1: "))
        s2 = float(input("Subject 2: "))
        s3 = float(input("Subject 3: "))

        # Validate marks
        if not (0 <= s1 <= 100 and 0 <= s2 <= 100 and 0 <= s3 <= 100):
            print("Marks must be between 0 and 100.")
            continue

        average = (s1 + s2 + s3) / 3

        # Determine grade
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # Count students
        student_count += 1
        total_class_average += average

        # Output
        print("-" * 30)
        print(f"Name    : {name}")
        print(f"Average : {average:.1f}")
        print(f"Grade   : {grade}")
        print("-" * 30)

    except ValueError:
        print("Error: Please enter numbers for the marks.")

# Final summary
print("\n" + "=" * 30)
print("Program Finished")

if student_count > 0:
    class_avg = total_class_average / student_count
    print(f"Students Entered : {student_count}")
    print(f"Class Average    : {class_avg:.2f}")
else:
    print("No student data entered.")

print("=" * 30)
