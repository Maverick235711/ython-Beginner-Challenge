
# TASK 1: Introduction

print("My name is Ayush")
print("My branch is CCE")
print("I am a first-year student at LNMIIT")
print("I am learning Python programming")


# TASK 2: Student Details

name = "Ayush"
roll_number = "26UCC005"
age = 18
cgpa = 8.5

print("\n--- Student Details ---")
print("Name:", name)
print("Roll Number:", roll_number)
print("Age:", age)
print("CGPA:", cgpa)


# TASK 3: Basic Calculator

print("\n--- Basic Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Division by zero is not possible")
