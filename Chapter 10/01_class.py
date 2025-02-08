class Employee:
    language = "C++"  #This is a class attribute
    salary = 100000
    
#Harry is an Object
#Employee is a class

harry  = Employee()
harry.name = "Haris Ali Khan" ##This is an object/instance attribute
print(harry.name,harry.language,harry.salary)

rohan  = Employee()
rohan.name = "Rohan Ali"
print(rohan.name,rohan.language,rohan.salary)

'''Here name is object/instance attributes , salary and language 
are class attributes as they directly belong to the class
'''