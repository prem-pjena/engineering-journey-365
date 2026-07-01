# Task 4: Remove duplicates manually (no set())

nums = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("Original:", nums)
print("Unique:", unique)
