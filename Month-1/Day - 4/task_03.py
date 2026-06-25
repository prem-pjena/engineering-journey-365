# Task 3: Word Input with break

print("=== Word Input ===")
print("Type 'quit' to exit.")

while True:
    word = input("Enter a word: ")
    if word == "quit":
        print("Goodbye!")
        break
    print(f"You entered: {word}")
