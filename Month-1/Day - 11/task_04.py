# Task 4: VectorStore with instance methods

class VectorStore:
    def __init__(self):
        self.documents = {}  # id -> document mapping
        self.next_id = 1
    
    def add_document(self, content):
        doc_id = self.next_id
        self.documents[doc_id] = content
        self.next_id += 1
        return doc_id
    
    def search(self, keyword):
        results = {}
        for doc_id, content in self.documents.items():
            if keyword.lower() in content.lower():
                results[doc_id] = content
        return results

# Usage
store = VectorStore()
store.add_document("Python is a programming language")
store.add_document("Java is also popular")
store.add_document("Machine learning with Python")

results = store.search("Python")
print(f"Found {len(results)} documents:")
for doc_id, content in results.items():
    print(f"  [{doc_id}] {content}")
