# Task 2: Division calculator with multiple exception handling

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except ValueError:
    print("❌ Please enter valid integers.")
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("✅ Calculation attempted.")
