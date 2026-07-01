# Task 3: Build a list using append() and user input

numbers = []

print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

print("\nYour numbers:", numbers)
print("Total count:", len(numbers))
