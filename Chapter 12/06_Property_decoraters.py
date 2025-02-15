class EMployee:
    a = 1 
    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")
    
    @property 
    def name (self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
e = EMployee()
e.a = 45
e.name = "Harry Khan"
print(e.fname,e.lname)
