# Task 3: Object attributes vs local variables

class Calculator:
    def __init__(self):
        self.history = []  # object attribute — persists
    
    def add(self, a, b):
        result = a + b      # local variable — temporary
        self.history.append(f"{a} + {b} = {result}")  # stored in object
        return result
    
    def show_history(self):
        return self.history

calc = Calculator()
print(calc.add(5, 3))       # 8
print(calc.add(10, 20))     # 30
print(calc.show_history())  # ['5 + 3 = 8', '10 + 20 = 30']
