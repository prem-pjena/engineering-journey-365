# Task 5: Python Package Structure Demo

"""
This file demonstrates the Module vs Package concepts.

Module = One .py file (like this one)
Package = Folder containing related modules

Example structure:
    utils/              ← Package
        __init__.py     ← Makes utils a package
        calculator.py   ← Module
        logger.py       ← Module
    main.py             ← Module
"""

# Calculator module functions
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Test calculator functions
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
