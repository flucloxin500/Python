''' Write a recursive function to calculate the sum of first n natural numbers.'''
# sum(n) = sum(n-1)+n

def sum(n) :
    if(n==1):
        return 1
    return sum(n-1) + n

x = int(input("Enter number for calculate it's total sum: "))

Natural = sum(x)
print(Natural)    