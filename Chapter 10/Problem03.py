'''Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute? '''

class Demo:
    a = 4
    
o = Demo()
o.a = 0 # Doesnot chaange class attribute

print(o.a)