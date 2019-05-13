from observer import *


class Date(Subscriber):
    def __init__(self):
        self.d ='' 
        self.m = ''
        self.y = ''
       
        Subscriber.__init__(self, "Date")
        pass

    def set(self, sentence):
        check = True
        split = sentence.split(',')
        d = int(split[9][0:2])
        m = int(split[9][2:4])
        y = int(split[9][4:6])

        if d<0 or d>31:
            check = False
        if m<0 or m>12:
            check = False
        if y<0 or y>99:
            check = False
        
        if check == True:
            self.d = d
            self.m = m
            self.y = y
    
    def get(self):
        print ("d:{} m:{} y:{}".format(self.d,self.m,self.y))

    def toString(self):
        return "Date()"
