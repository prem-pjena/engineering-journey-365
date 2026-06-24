# Task 2: Discount Checker (using `or`)
# Checks if a customer qualifies for a discount: loyalty member OR first-time buyer

print("=== Discount Checker ===")

is_loyalty = input("Are you a loyalty member? (yes/no): ").lower()
is_first_time = input("Are you a first-time buyer? (yes/no): ").lower()

if is_loyalty == "yes" or is_first_time == "yes":
    print("🎉 You qualify for a discount!")
else:
    print("❌ Sorry, no discount available.")
