'''Write a program to find out whether a file is identical & matches the content of 
another file. '''

with open(r"E:\Python\All Projects\Chapter 9\Hi-Score.txt") as f:
    content1 = f.read()
with open(r"E:\Python\All Projects\Chapter 9\log.txt") as f:
    content2 = f.read()


if ( content1 == content2):
    print("The content of both files are identical")

else:
    print("The content of both files are not identical")