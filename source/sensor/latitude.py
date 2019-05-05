from GPS_Mediator import *

class Latitude(Colleague):
    def __init__(self, mediator, identity):
        self.lat =''
        self.latitude_pos = 2
        super().__init__(mediator, identity)
        pass

    def set(self, sentence):
        split =sentence.split(',') 
        print (split)

    def get(self):
        return self.lat

    def toString(self):
        return "Latitude()"

    def send(self, message):
        print("Message '" + message + "' sent by Colleague " + str(self._id))
        self._mediator.distribute(self, message)
    
    def receive(self, message):
        print("Message '" + message + "' received by Colleague " + str(self._id))