# Task 5: Password Retry System

print("=== Password Retry System ===")
VALID_PASSWORD = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == VALID_PASSWORD:
        print("✅ Access granted!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Wrong password. {remaining} attempt(s) left.")
        else:
            print("🔒 Account locked. Too many failed attempts.")
