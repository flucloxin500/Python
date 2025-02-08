'''Create a class “Programmer” for storing information of few programmers 
working at Microsoft. '''

class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = Programmer("Walid",45000,4205)
print(p.name,p.salary,p.pin,p.company)
r = Programmer("Harry",45000,4205)
print(r.name,r.salary,r.pin,r.company)
