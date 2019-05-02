from observer import *


class Longitude(Subscriber):
    def __init__(self):
        self.lon =''
        Subscriber.__init__(self, "Longitude")

    def set(self, value):
        self.lon = value

    def get(self):
        return self.lon
    
    def toString(self):
        return "Longitude()"