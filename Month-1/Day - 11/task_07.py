# Task 7: super() — calling parent constructors

class VectorStore:
    def __init__(self):
        self.documents = {}
        self.next_id = 1
        print("VectorStore initialized")

class PersistentVectorStore(VectorStore):
    def __init__(self, file_path):
        super().__init__()  # Calls VectorStore.__init__ to set up documents and next_id
        self.file_path = file_path
        print(f"PersistentVectorStore saving to {file_path}")

# super() ensures parent initializes shared attributes
# Child initializes additional attributes
store = PersistentVectorStore("/data/store.json")
print(f"Documents dict: {store.documents}")
print(f"File path: {store.file_path}")
