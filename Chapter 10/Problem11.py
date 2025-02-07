'''Write a python program to rename a file to “renamed_by_ python.txt. '''

with open (r"E:\Python\All Projects\CHapter 9\old.txt","r") as f:
    content = f.read()
    
with open (r"E:\Python\All Projects\CHapter 9\renamed_by_python.txt","w") as f:
    f.write(content)