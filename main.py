


def add_student():

    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()

    # Check empty values
    if name == "" or roll_number == "":
        print("Name and roll number cannot be empty!")
        return

    # Avoid commas because commas separate the saved fields
    if "," in name or "," in roll_number:
        print("Name and roll number cannot contain commas!")
        return

    # Validate marks
    try:
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Invalid input! Please enter numeric marks.")
        return

    # Check whether roll number already exists
    try:
        with open("students.txt", "r") as file:

            for student in file:
                details = student.strip().split(",")

                if len(details) == 3:
                    if details[1] == roll_number:
                        print("A student with this roll number already exists!")
                        return

    except FileNotFoundError:
        pass

    # Save student details
    with open("students.txt", "a") as file:
        file.write(name + "," + roll_number + "," + str(marks) + "\n")

    print("Student added successfully!")


# FEATURE 2: VIEW ALL STUDENTS

def view_students():

    print("\n--- All Students ---")

    try:
        with open("students.txt", "r") as file:

            students = file.readlines()

            if len(students) == 0:
                print("No student records found.")
                return

            found = False

            for student in students:

                details = student.strip().split(",")

                if len(details) != 3:
                    print("Skipping an invalid record.")
                    continue

                name = details[0]
                roll_number = details[1]
                marks = details[2]

                print("\nName:", name)
                print("Roll Number:", roll_number)
                print("Marks:", marks)
                print("-------------------------")

                found = True

            if found == False:
                print("No valid student records found.")

    except FileNotFoundError:
        print("Student file does not exist yet.")


# FEATURE 3: SEARCH STUDENT BY ROLL NUMBER

def search_student():

    print("\n--- Search Student ---")

    search_roll = input("Enter roll number to search: ").strip()

    found = False

    try:
        with open("students.txt", "r") as file:

            for student in file:

                details = student.strip().split(",")

                if len(details) != 3:
                    continue

                name = details[0]
                roll_number = details[1]
                marks = details[2]

                if roll_number == search_roll:

                    print("\nStudent Found!")
                    print("Name:", name)
                    print("Roll Number:", roll_number)
                    print("Marks:", marks)

                    found = True
                    break

            if found == False:
                print("Student not found!")

    except FileNotFoundError:
        print("Student file does not exist yet.")


# FEATURE 4: CALCULATE AVERAGE MARKS

def calculate_average():

    print("\n--- Calculate Average Marks ---")

    try:
        with open("students.txt", "r") as file:

            total = 0
            count = 0

            for student in file:

                details = student.strip().split(",")

                if len(details) != 3:
                    continue

                try:
                    marks = float(details[2])

                    total = total + marks
                    count = count + 1

                except ValueError:
                    print("Skipping a record with invalid marks.")

            if count == 0:
                print("No valid student records found.")

            else:
                average = total / count

                print("Total Students:", count)
                print("Average Marks:", round(average, 2))

    except FileNotFoundError:
        print("Student file does not exist yet.")


# MAIN MENU

def main():

    while True:

        print("\n========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Calculate Average Marks")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            calculate_average()

        elif choice == "5":
            print("\nThank you for using Student Management System!")
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


# START THE PROGRAM

if __name__ == "__main__":
    main()
