class Employee:
    language = "C++"  #This is a class attribute
    salary = 100000
    
    def __init__(self,name,language,salary):#Dunder method, which is automatically called
        self.name = name 
        self.language = language
        self.salary = salary
        print("I'm Creating an object")
    
    def getInfo(self):
        print(f"The lang is: {self.language}. The salary is: {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning!")
        
    


harry  = Employee("Walid","C#",25000)
harry.name = "Haris Ali Khan"
print(harry.name , harry .salary , harry.language)

#walid = Employee()