# Task 4: Accumulator pattern — sum of list without sum()

numbers = [10, 25, 33, 47, 52]

total = 0
for num in numbers:
    total += num

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", total / len(numbers))
