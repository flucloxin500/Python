class Employee:
    language = "C++"  #This is a class attribute
    salary = 100000
    
#Harry is an Object
#Employee is a class

harry  = Employee()
harry.language = "GoLang" #Instance attributes, take preference over class attributes during assignment & retrieval.
print(harry.language,harry.salary)
