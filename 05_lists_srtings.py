
# TASK 1: Subject List

subjects = ["Maths", "Physics", "Python", "English", "Electronics"]

print("--- My Subjects ---")

for subject in subjects:
    print(subject)


# TASK 2: Marks Calculator

print("\n--- Marks Calculator ---")

marks = []

for i in range(5):
    m = float(input("Enter marks: "))
    marks.append(m)

print("Total:", sum(marks))
print("Average:", sum(marks) / 5)
print("Highest:", max(marks))
print("Lowest:", min(marks))


# TASK 3: Student Dictionary

print("\n--- Student Details ---")

student = {
    "name": "Ayush",
    "roll_number": "26UCC005",
    "marks": 85
}

print("Name:", student["name"])
print("Roll Number:", student["roll_number"])
print("Marks:", student["marks"])


# TASK 4: Search a Name

print("\n--- Name Search ---")

names = ["Ayush", "Rahul", "Aman", "Rohit"]

search_name = input("Enter name to search: ")

if search_name in names:
    print("Name found!")
else:
    print("Name not found!")


# TASK 5: Character Frequency

print("\n--- Character Frequency ---")

word = input("Enter a string: ")

frequency = {}

for ch in word:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in frequency:
    print(ch, ":", frequency[ch])
