'''Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50        
=> F '''

d = {}

name = input("Enter friends name: ")
lang = input("Enter lang name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter lang name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter lang name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter lang name: ")
d.update({name: lang})

print(d)