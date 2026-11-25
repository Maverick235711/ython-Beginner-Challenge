
# TASK 1: Write and Read a File

print("--- File Writing and Reading ---")

with open("hello.txt", "w") as file:
    file.write("Hello Ayush!\n")
    file.write("I am learning Python.")

with open("hello.txt", "r") as file:
    content = file.read()

print(content)


# TASK 2: Save Student Details

print("\n--- Student Details ---")

name = input("Enter student name: ")
marks = input("Enter student marks: ")

with open("students.txt", "a") as file:
    file.write(name + "," + marks + "\n")

print("Student details saved successfully!")

with open("students.txt", "r") as file:
    print("\nSaved Student Records:")
    print(file.read())


# TASK 3: Handle Invalid Numeric Input

print("\n--- Error Handling ---")

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Invalid input! Please enter a number.")


# TASK 4: Handle Missing or Empty Files

print("\n--- File Checking ---")

try:
    with open("students.txt", "r") as file:
        content = file.read()

        if content.strip() == "":
            print("The file is empty.")

        else:
            print("File contents:")
            print(content)

except FileNotFoundError:
    print("The file does not exist.")
