from observer import *


class Latitude(Subscriber):
    def __init__(self): 
        self.lat =''
        self.N_S = ''
        self.latitude_pos = 3
        self.N_S_pos = 4
        Subscriber.__init__(self, "Latitude")
        pass

    def set(self, sentence):
        split =sentence.split(',') 
        self.lat = split[self.latitude_pos]
        self.N_S = split[self.N_S_pos]

        #print(self.lat)
        #print(self.N_S)
        
        #print (split)

    def get(self):
        return self.lat

    def toString(self):
        return "Latitude()"
