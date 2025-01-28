'''Write a program to find the sum of first n natural numbers using while loop.'''

i = 0 
n = int (input("Enter a natural number: "))
sum = 0
while ( i <= n ):
    sum += i 
    i += 1
print(sum)