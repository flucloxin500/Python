'''Write a program to mine a log file and find out whether it contains ‘python’. '''

with open(r"E:\Python\All Projects\Chapter 9\log.txt", "r") as f:
    content = f.read()
    
if ("python" in content):
    print("The word 'python' is found in the log file.")

else:
    print("The word 'python' is not found in the log file.")