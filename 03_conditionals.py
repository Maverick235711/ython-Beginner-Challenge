
# TASK 1: Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# TASK 2: Grade Calculator

print("\n--- Grade Calculator ---")

marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# TASK 3: Leap Year

print("\n--- Leap Year Checker ---")

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# TASK 4: Simple Calculator

print("\n--- Simple Calculator ---")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
