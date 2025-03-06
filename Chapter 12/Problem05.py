'''  Store the multiplication tables generated in problem 3 in a file named Tables.txt. '''


n = int(input("Enter the number for it's multiplication table: "))
table = [n*i for i in range(1,11)]

with open(r"E:\Python\All Projects\Chapter 12\tables.txt", "a") as f:
        f.write(str(table)+ "\n")

