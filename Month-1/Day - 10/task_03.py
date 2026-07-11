# Task 3: Exception handling with files

def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"❌ {filename} not found. Returning empty list.")
        return []
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return []

data = read_file_safe("nonexistent.txt")
print("Data:", data)
