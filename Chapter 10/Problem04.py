'''Add a static method in problem 2, to greet the user with hello. '''



class Calculator:
    def __init__(self, n):
        self.n = n
        
    def Sqaure(self):
        print(f"The square is {self.n * self.n}")
        
    def Cube(self):
        print(f"The cube is {self.n * self.n * self.n}")
        
    def SqaureRoot(self):
        print(f"The square root is {self.n **1/2}")
    
    @staticmethod
    def greet():
        print("Hello World!")
        

X = Calculator(4)
X.Sqaure()
X.Cube()
X.SqaureRoot()
X.greet()
