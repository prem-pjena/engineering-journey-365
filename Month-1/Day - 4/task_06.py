# Task 6: Menu-Driven Application

print("=== Menu System ===")

while True:
    print("\n--- Main Menu ---")
    print("1. Say Hello")
    print("2. Show Date")
    print("3. Tell a Joke")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        print("👋 Hello there!")
    elif choice == "2":
        print("📅 Today is a great day to code!")
    elif choice == "3":
        print("😂 Why do programmers prefer dark mode? Because light attracts bugs!")
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid option. Please try again.")
