# Task 6: Method overriding

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):  # Override parent's speak method
        return f"{self.name} barks!"

class Cat(Animal):
    def speak(self):  # Override parent's speak method
        return f"{self.name} meows!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy barks! (overridden)
print(cat.speak())  # Whiskers meows! (overridden)

# Runtime lookup: Python looks for the method on the object's class FIRST
# If not found, it goes up to the parent class
