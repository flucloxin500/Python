try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as E:
    print(E)
    
else:
    print("No exception occurred")
