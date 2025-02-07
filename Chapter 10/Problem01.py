'''Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’. '''

with open(r"E:\Python\All Projects\Chapter 9\Poem.txt") as f:
    text = f.read()
    
    if ("twinkle" in text):
        print("Twinkle is present")
    else:
        print("Twinkle is not present")
        
f.close()