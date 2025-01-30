'''  Write a python program using function to convert Celsius to Fahrenheit. '''
def fahrenheit(C):
    F = (C * 9/5) + 32
    return F

celcius = int(input("enter the celcius tempo: "))

a = round(fahrenheit(celcius),2)
print(a)
