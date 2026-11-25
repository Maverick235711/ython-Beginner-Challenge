
# TASK 1: Data Types

age = 18
cgpa = 8.5
name = "Ayush"
is_student = True

print("--- Data Types ---")
print(age, type(age))
print(cgpa, type(cgpa))
print(name, type(name))
print(is_student, type(is_student))


# TASK 2: Celsius to Fahrenheit

print("\n--- Temperature Converter ---")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9/5) * celsius + 32

print("Temperature in Fahrenheit:", fahrenheit)


# TASK 3: Rectangle Calculator

print("\n--- Rectangle Calculator ---")

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area:", area)
print("Perimeter:", perimeter)


# TASK 4: Comparison and Logical Operators

print("\n--- Operators ---")

a = 10
b = 20

print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)

print("AND:", a < b and b > 15)
print("OR:", a > b or b > 15)
print("NOT:", not(a > b))
