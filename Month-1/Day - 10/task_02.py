# Task 2: File I/O — Contact persistence

def save_contacts(contacts, filename="contacts.txt"):
    with open(filename, "a") as f:
        for contact in contacts:
            f.write(contact + "\n")

def load_contacts(filename="contacts.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Test
contacts = load_contacts()
print("Existing contacts:", contacts)

new = ["Alice", "Bob", "Charlie"]
save_contacts(new)

contacts = load_contacts()
print("After save:", contacts)
