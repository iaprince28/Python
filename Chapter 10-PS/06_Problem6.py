from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time")

    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Benapole", "Kashmir")        
t.getStatus()        
t.getFare("Benapole", "Kashmir")        