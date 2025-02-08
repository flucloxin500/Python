'''Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. '''

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    def book(slf, fro , to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")
    
    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time")
    
    def getFare(self, fro , to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(5000,7215)}")
    

t = Train(12364)

t.book("CTG","DHK")
t.getFare("CTG","DHK")
t.getStatus()