'''Repeat program 4 for a list of such words to be censored.'''

words = ["Doneky","bad","crucial","rude"]

with open(r"E:\Python\All Projects\Chapter 9\file.txt", "r") as f:
    content = f.read()

for word in words :
    content = content.replace(word, "#" * len(word))



with open(r"E:\Python\All Projects\Chapter 9\file.txt", "w") as f:
    f.write(content)