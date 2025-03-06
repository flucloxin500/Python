try:
    a = int(input("Hey, Enter a number: "))
    print(a)
    
except ValueError as V:
    print("Invalid input. Please enter a valid number.")

except Exception as e:
    print("Thank you!")
    
# a = int(input("Hey, Enter a number: "))
# print(a)