# Task 2: Membership operators

fruits = ["apple", "banana", "mango", "orange"]

fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print(f"✅ {fruit} is in the list!")
else:
    print(f"❌ {fruit} is NOT in the list.")
