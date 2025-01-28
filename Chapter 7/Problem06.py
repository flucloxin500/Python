'''Write a program to calculate the factorial of a given number using for loop. '''

i = 1
n = int (input("Enter a natural number: "))
product = 1
while ( i <= n ):
    product *= i 
    i += 1
    
print(product)