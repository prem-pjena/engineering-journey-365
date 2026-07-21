# Task 2: __init__ and self deep dive

class Student:
    def __init__(self, name, age):
        # self refers to the current object being created
        self.name = name      # object attribute
        self.age = age        # object attribute
        print(f"Created student: {self.name}")
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# self = prem when we call Student("Prem", 24)
prem = Student("Prem", 24)
print(prem.introduce())

# self = john when we call Student("John", 22)
john = Student("John", 22)
print(john.introduce())
