# Task 1: File I/O basics — read, write, append

# Write mode
with open("sample.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is line 2.\n")

# Read mode
with open("sample.txt", "r") as f:
    content = f.read()
    print("Full file:")
    print(content)

# Append mode
with open("sample.txt", "a") as f:
    f.write("This is appended.\n")

# Read lines
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("Lines:")
    for line in lines:
        print(repr(line))
