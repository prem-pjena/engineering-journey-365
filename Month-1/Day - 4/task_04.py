# Task 4: Skip-Number Program using continue

print("=== Skip Even Numbers ===")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)
