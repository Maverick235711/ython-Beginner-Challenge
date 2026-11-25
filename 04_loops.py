
# TASK 1: Print numbers from 1 to 100

print("--- Numbers from 1 to 100 ---")

for i in range(1, 101):
    print(i)


# TASK 2: Multiplication Table

print("\n--- Multiplication Table ---")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# TASK 3: Sum of numbers from 1 to N

print("\n--- Sum of Numbers ---")

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


# TASK 4: Count Vowels

print("\n--- Vowel Counter ---")

word = input("Enter a word: ")

count = 0

for ch in word:
    if ch.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)


# TASK 5: Prime Numbers from 1 to 100

print("\n--- Prime Numbers ---")

for num in range(2, 101):

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
