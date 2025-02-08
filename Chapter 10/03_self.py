class Employee:
    language = "C++"  #This is a class attribute
    salary = 100000
    
    def getInfo(self):
        print(f"The lang is: {self.language}. The salary is: {self.salary}")
    
    #@staticmethod it allows no parameter as object
    def greet(self):
        print("Good Morning!")
        
    


harry  = Employee()
harry.language = "GoLang" #Instance attributes, take preference over class attributes during assignment & retrieval.
harry.getInfo()
Employee.getInfo(harry) #harry as a parameter pass the object of class
harry.greet()
Employee.greet(harry)
