a = int(input("Hey, Enter a number: "))
b = int(input("Hey, Enter the second number: "))

if ( b == 0):
    raise ZeroDivisionError ("Hey our program is not meant to divide numbers by zero")

else:
    print(f"The division a/b is {a/b}")