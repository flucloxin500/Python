class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3
    
O = Manager()

print(O.a)
print(O.b)
print(O.c)