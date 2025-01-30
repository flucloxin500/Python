''' Write a python function which converts inches to cms. '''

def converter(inch):
    # 1 inch is equal to 2.54 cm
    return inch * 2.54

In = float(input("Enter the inches: "))
print(converter(In))  # Output: 10.16

