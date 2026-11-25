
# TASK 1: Largest of Three Numbers

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("--- Largest Number ---")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest:", largest(x, y, z))


# TASK 2: Prime Number Checker

def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print("\n--- Prime Checker ---")

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")


# TASK 3: Average Marks

def calculate_average(marks):

    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)

print("\n--- Average Marks ---")

marks = [85, 90, 78, 88, 92]

print("Average:", calculate_average(marks))


# TASK 4: Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("\n--- Calculator ---")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", add(a, b))

elif operator == "-":
    print("Result:", subtract(a, b))

elif operator == "*":
    print("Result:", multiply(a, b))

elif operator == "/":
    print("Result:", divide(a, b))

else:
    print("Invalid operator")
