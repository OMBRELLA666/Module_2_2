
def main():
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            print("Exiting program.")
            break

        first_name = input("Enter student's first name: ")

        try:
            gpa = float(input("Enter student's GPA: "))
        except ValueError:
            print("Invalid GPA input. Please enter a numeric value.")
            continue

        print(f"\nStudent: {first_name} {last_name}")
        if gpa >= 3.5:
            print("Congratulations! You've made the Dean's List.")
        elif gpa >= 3.25:
            print("Great job! You've made the Honor Roll.")
        else:
            print("Keep working hard!")

        print("-" * 40)

if __name__ == "__main__":
    main()