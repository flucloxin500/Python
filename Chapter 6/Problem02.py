#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

phy = int(input("Enter your physics number: "))

chem = int(input("Enter your chemistry number: "))

bio = int(input("Enter your bilogy number: "))

avg = ((phy+chem+bio))/3

if (avg>=40 and phy >= 33 and bio >= 33 and chem >= 33):
    print("You're pass!")
    
else:
    print("Better luck next time!")