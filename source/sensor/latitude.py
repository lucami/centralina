from observer import *


class Latitude(Subscriber):
    def __init__(self):
        self.lat =''
        self.latitude_pos = 2
        Subscriber.__init__(self, "Latitude")
        pass

    def set(self, sentence):
        split =sentence.split(',') 
        print (split)

    def get(self):
        return self.lat

    def toString(self):
        return "Latitude()"
