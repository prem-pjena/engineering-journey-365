# Task 5: Find largest number manually without max()

numbers = [45, 12, 78, 34, 91, 23]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Numbers:", numbers)
print("Largest number:", largest)
