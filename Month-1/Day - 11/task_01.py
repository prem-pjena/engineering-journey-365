# Task 1: Classes & Objects — Car blueprint

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        return f"{self.brand} {self.model}"

# Creating objects (instances)
bmw = Car("BMW", "X5")
audi = Car("Audi", "Q7")

print(bmw.display())  # BMW X5
print(audi.display())  # Audi Q7
