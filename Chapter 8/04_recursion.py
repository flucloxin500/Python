'''
fact(1) = 1 
fact(2) = 1 X 2
fact(3) = 1 X 2 X 3
fact(4) = 1 X 2 X 3 X 4
fact(5) = 1 X 2 X 3 X 4 X 5

fact(n) = n * (fact(n-1))
'''

def factorial(n):
    if ( n == 1 or n == 0) :
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))

print(f"The factorial of {n} is : {factorial(n)}")