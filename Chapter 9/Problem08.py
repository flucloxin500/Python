'''Write a program to make a copy of a text file “this. txt” '''

with open (r"E:\Python\All Projects\Chapter 9\this.txt","r") as f:
    content = f.read()
    
with open (r"E:\Python\All Projects\Chapter 9\this_copy.txt","w") as f:
    f.write(content)