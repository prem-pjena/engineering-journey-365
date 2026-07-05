# Task 8: Calculator 2.0 — with function dispatch table


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero"
    return a / b


operations = {1: add, 2: subtract, 3: multiply, 4: divide}


def main():
    while True:
        print("\n===== CALCULATOR 2.0 =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Choose (1-5): ")

        if choice == "5":
            print("Goodbye! 👋")
            break

        if choice not in ("1", "2", "3", "4"):
            print("❌ Invalid choice.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        result = operations[int(choice)](a, b)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
