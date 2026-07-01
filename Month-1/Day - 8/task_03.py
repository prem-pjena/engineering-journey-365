# Task 3: List comprehensions

# Squares of 1-10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# Even numbers 1-20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Evens:", evens)

# Uppercase fruits
fruits = ["apple", "banana", "mango", "orange"]
upper = [f.upper() for f in fruits]
print("Uppercase:", upper)
