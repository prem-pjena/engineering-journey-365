# Task 6: Lists of dictionaries + Linear Search

students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [72, 88, 95]},
    {"name": "Charlie", "scores": [90, 92, 88]}
]

# Calculate average for each
for student in students:
    avg = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: Average = {avg:.1f}")

# Linear search by name
search = input("\nSearch student by name: ")
found = False
for student in students:
    if student["name"].lower() == search.lower():
        avg = sum(student["scores"]) / len(student["scores"])
        print(f"✅ Found {student['name']} — Average: {avg:.1f}")
        found = True
        break

if not found:
    print("❌ Student not found.")
