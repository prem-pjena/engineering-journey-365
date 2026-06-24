# Task 5: Login + Role Validation System (Bonus)
# Advanced version with role-based access

print("=== Advanced Login System ===")
print()

VALID_USERNAME = "admin"
VALID_PASSWORD = "pass123"
ADMIN_USERNAME = "admin"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("✅ Login Successful!")
        if username == ADMIN_USERNAME:
            print("👑 Welcome, Admin! You have full access.")
            print("   - Manage Users")
            print("   - View Reports")
            print("   - System Settings")
        else:
            print("👤 Welcome, User!")
            print("   - View Profile")
            print("   - Browse Content")
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
