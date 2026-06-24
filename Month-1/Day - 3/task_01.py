# Task 1: Eligibility Checker (using `and`)
# Checks if a person is eligible for a job: age >= 18 AND has a degree

print("=== Job Eligibility Checker ===")

age = int(input("Enter your age: "))
has_degree = input("Do you have a degree? (yes/no): ").lower()

if age >= 18 and has_degree == "yes":
    print("✅ You are eligible for the job!")
else:
    print("❌ You are not eligible.")
    if age < 18:
        print("   Reason: You must be at least 18 years old.")
    if has_degree != "yes":
        print("   Reason: A degree is required.")
