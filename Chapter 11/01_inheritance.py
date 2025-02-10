class Employee:
    company ="Brain Station"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
# class Programmer:
#     company ="Brain Station 23"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
        
#     def showlanguage(self):
#         print(f"The nameis {self.name} and he is good at {self.language} language")

class Programmer(Employee):
    company ="Brain Station 23"
    def showlanguage(self):
        print(f"The nameis {self.name} and he is good at {self.language} language")
   
a = Employee()

b = Programmer()

print(a.company , b.company)