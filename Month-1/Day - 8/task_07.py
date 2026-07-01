# Mini Project: Contact Book

contacts = []

def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts.append({"name": name, "phone": phone})
    print(f"✅ Added {name}")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
        return
    print("\nYour contacts:")
    for i, c in enumerate(contacts):
        print(f"{i+1}. {c['name']} — {c['phone']}")

def search_contact():
    name = input("Search name: ").lower()
    found = False
    for c in contacts:
        if c["name"].lower() == name:
            print(f"✅ Found: {c['name']} — {c['phone']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").lower()
    found = False
    for i, c in enumerate(contacts):
        if c["name"].lower() == name:
            contacts.pop(i)
            print(f"🗑️ Deleted {c['name']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

while True:
    show_menu()
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice.")
