# Task 8: Static methods and class methods

class MathUtils:
    pi = 3.14159  # class attribute — shared by all objects
    
    @staticmethod
    def add(a, b):
        # No self, no cls — just a utility function in the class namespace
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @classmethod
    def circle_area(cls, radius):
        # cls refers to the class itself, can access class attributes
        return cls.pi * radius * radius
    
    @classmethod
    def set_pi(cls, value):
        cls.pi = value

# Static methods — no object needed
print(MathUtils.add(5, 3))       # 8
print(MathUtils.multiply(4, 7))  # 28

# Class methods — access shared class state
print(MathUtils.circle_area(5))  # 78.53975
MathUtils.set_pi(3.14)
print(MathUtils.circle_area(5))  # 78.5

# When to use what:
# - Instance method: needs object data (self)
# - Static method: utility, no object/class data needed
# - Class method: needs shared class data (cls)
