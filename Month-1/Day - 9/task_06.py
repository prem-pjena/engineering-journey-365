# Task 6: map() and filter()

numbers = [5, 10, 15, 20]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Original: {numbers}")
print(f"Doubled (map): {doubled}")

nums = [11, 12, 13, 14, 15, 16]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Original: {nums}")
print(f"Evens (filter): {evens}")
