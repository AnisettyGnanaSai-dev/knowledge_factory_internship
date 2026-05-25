class MathOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mathOperation(self):
        return self.a + self.b
    
class Subtraction(MathOperation):
    def mathOperation(self):
        return self.a - self.b
    
add = MathOperation(10, 5)
subtract = Subtraction(10, 5)
print(add.mathOperation())      # Output: 15
print(subtract.mathOperation()) # Output: 5