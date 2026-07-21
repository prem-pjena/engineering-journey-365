# Task 5: Inheritance basics

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):  # Dog inherits from Animal
    pass  # Dog gets everything from Animal

class Cat(Animal):  # Cat inherits from Animal
    pass

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy makes a sound (inherited!)
print(cat.speak())  # Whiskers makes a sound (inherited!)
