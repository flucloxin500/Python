'''Write a program using functions to find greatest of three numbers. '''

def greatest(a,b,c):
    if (a >= b and a >= c):
        return a
    elif (b >= a and b >= c):
        return b
    else:
        return c
    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("The greatest number is: ", greatest(num1, num2, num3))
        