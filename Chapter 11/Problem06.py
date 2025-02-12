''' Write __str__() method to print the vector as follows: 
7i + 8j +10k  
Assume vector of dimension 3 for this problem. '''

class Vector:
    def __init__(self,l):
        self.l = l
        
    
    def __len__(self):
        return len(self.l)
    

v1 = Vector([1,2,3])

print(len(v1))

