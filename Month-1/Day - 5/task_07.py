# Task 7: Reverse a string using a for loop (no slicing)

text = input("Enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(f"Reversed: {reversed_text}")
