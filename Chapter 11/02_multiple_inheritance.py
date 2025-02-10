class Employee:
    company ="Brain Station"
    name = "Default"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printlanguage(self):
        print(f"Out of all languages here is your language: {self.language}")

class Programmer(Employee,Coder):
    company ="Brain Station 23"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good at {self.language} language")
   

b = Programmer()

b.show()
b.showlanguage()
b.printlanguage()