# Task 1: Handle invalid integer input using try/except

try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")
