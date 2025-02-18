try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as E:
    print(E)
    
finally: #will run in any time. also in function
    print("No exception occurred")
