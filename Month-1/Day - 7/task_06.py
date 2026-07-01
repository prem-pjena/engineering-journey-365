# Task 6: Use pop(), remove(), insert()

tasks = ["Learn Python", "Practice DSA", "Build Project", "Apply for Jobs"]
print("Initial list:", tasks)

# remove() — remove by value
tasks.remove("Practice DSA")
print("After remove:", tasks)

# pop() — remove by index (last item)
removed = tasks.pop()
print(f"Popped: '{removed}'")
print("After pop:", tasks)

# insert() — insert at specific position
tasks.insert(1, "Update Resume")
print("After insert:", tasks)
