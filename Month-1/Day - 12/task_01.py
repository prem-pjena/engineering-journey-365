# Task 1: SafeFileManager — Custom Context Manager

class SafeFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            print(f"Opened {self.filename}")
            return self.file
        except FileNotFoundError:
            print(f"Error: {self.filename} not found")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"Closed {self.filename}")
        # Return False to propagate any exception that occurred
        return False

# Usage
with SafeFileManager("sample.txt", "w") as f:
    f.write("Hello from SafeFileManager!\n")

with SafeFileManager("sample.txt", "r") as f:
    content = f.read()
    print(content)
