st = "Hey walid, You are amazing!"

f = open(r"E:\Python\All Projects\Chapter 9\Myfile.txt", "w")

f.write(st)

f.close()

# FIle reading from written file
f = open(r"E:\Python\All Projects\Chapter 9\Myfile.txt", "r")

data = f.read()

print(data)

f.close()