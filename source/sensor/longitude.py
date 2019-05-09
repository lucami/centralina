from observer import *


class Longitude(Subscriber):
    def __init__(self):
        self.lon ='' 
        self.E_W = ''
        self.longitude_pos = 5
        self.E_W_pos = 6
        Subscriber.__init__(self, "Longitude")
        pass

    def set(self, sentence):
        split =sentence.split(',') 
        self.lon = split[self.longitude_pos]
        self.E_W = split[self.E_W_pos]

        print(self.lon)
        print(self.E_W)
        
        #print (split)

    def get(self):
        return self.lon

    def toString(self):
        return "Longitude()"
