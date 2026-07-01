# Mini Project: Todo List Manager

todos = []

while True:
    print("\n===== TODO LIST =====")
    print("1. Add task")
    print("2. Remove task")
    print("3. View all tasks")
    print("4. Exit")
    
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        task = input("Enter task: ")
        todos.append(task)
        print(f"✅ Added: {task}")
    
    elif choice == "2":
        if len(todos) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todos):
                print(f"{i+1}. {task}")
            idx = int(input("Enter task number to remove: "))
            if 1 <= idx <= len(todos):
                removed = todos.pop(idx - 1)
                print(f"🗑️ Removed: {removed}")
            else:
                print("❌ Invalid number")
    
    elif choice == "3":
        if len(todos) == 0:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todos):
                print(f"{i+1}. {task}")
    
    elif choice == "4":
        print("Goodbye! 👋")
        break
    
    else:
        print("❌ Invalid choice. Try again.")
