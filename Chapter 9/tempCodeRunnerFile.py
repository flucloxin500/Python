'''f = open(r"E:\Python\All Projects\Chapter 9\file.txt", "r")
print(f.read())
f.close()'''

with open(r"E:\Python\All Projects\Chapter 9\file.txt", "r") as f:
    print(f.read())