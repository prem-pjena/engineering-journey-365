# Task 4: Login Validation System
# Combines all concepts — and, or, not, nested conditions

print("=== Login Validation System ===")
print("Enter credentials to log in.")
print()

VALID_USERNAME = "admin"
VALID_PASSWORD = "pass123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("✅ Login Successful! Welcome, admin.")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        
        if username != VALID_USERNAME and password != VALID_PASSWORD:
            print("❌ Both username and password are incorrect.")
        elif username != VALID_USERNAME:
            print("❌ Username not found.")
        else:
            print("❌ Wrong password.")
        
        if remaining > 0:
            print(f"   Attempts remaining: {remaining}")
        else:
            print("🔒 Account locked. Too many failed attempts.")
