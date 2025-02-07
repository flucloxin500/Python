'''A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.  '''

word = "Doneky"

with open(r"E:\Python\All Projects\Chapter 9\file.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey","######")


with open(r"E:\Python\All Projects\Chapter 9\file.txt", "w") as f:
    f.write(contentNew)