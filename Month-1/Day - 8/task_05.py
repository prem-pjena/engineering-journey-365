# Task 5: Dictionaries — create, access, update

person = {
    "name": "Prem",
    "age": 24,
    "city": "Bhubaneswar"
}

print("Name:", person["name"])
print("Age:", person.get("age"))
print("City:", person.get("city"))

# Update
person["age"] = 25
person["job"] = "AI Engineer"
print("\nUpdated:", person)

# Loop through keys, values, items
print("\nKeys:", list(person.keys()))
print("Values:", list(person.values()))
for key, value in person.items():
    print(f"  {key}: {value}")
