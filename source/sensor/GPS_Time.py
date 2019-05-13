from observer import *


class Time(Subscriber):
    def __init__(self):
        self.h ='' 
        self.m = ''
        self.s = ''
       
        Subscriber.__init__(self, "Time")
        pass

    def set(self, sentence):
       pass

    def get(self):
        return self.lon

    def toString(self):
        return "Longitude()"
