from GPS_Mediator import *

class Longitude(Colleague):
    def __init__(self, mediator, identity):
        self.lon =''
        self.longitude_pos = 1
        super().__init__(mediator, identity)

    def set(self, value):
        self.lon = value

    def get(self):
        return self.lon
    
    def toString(self):
        return "Longitude()"

    def send(self, message):
        print("Message '" + message + "' sent by Colleague " + str(self._id))
        self._mediator.distribute(self, message)

    def receive(self, message):
        print("Message '" + message + "' received by Colleague " + str(self._id))