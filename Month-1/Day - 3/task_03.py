# Task 3: Movie Entry System (Nested Conditions)
# Checks age and hasID before allowing entry

print("=== Movie Entry System ===")

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower()

if age >= 18:
    if has_id == "yes":
        print("🍿 Welcome! You can enter the movie.")
    else:
        print("❌ Entry denied. ID is required.")
else:
    print("❌ Entry denied. You must be 18 or older.")
