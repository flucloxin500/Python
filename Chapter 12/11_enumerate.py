l = [3,53,25,98,100]

# index = 0
# for item in l:
#     print(f"The item number: {index} is {item}")
#     index += 1
#This can be simplified by using enumerate

for index , item in enumerate(l):
    print(f"The item number: {index} is {item}")