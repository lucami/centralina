from observer import *


class Time(Subscriber):
    def __init__(self):
        self.h = '' 
        self.m = ''
        self.s = ''
       
        Subscriber.__init__(self, "Time")
        pass

    def set(self, sentence):
        check = True
        split = sentence.split(',')
        h = int(split[1][0:2])
        m = int(split[1][2:4])
        s = int(split[1][4:6])

        if h<0 or h>23:
            check = False
        if m<0 or m>60:
            check = False
        if s<0 or s>60:
            check = False
        
        if check == True:
            self.h = h
            self.m = m
            self.s = s
    
    def get(self):
        return ("h:{} m:{} s:{}".format(self.h,self.m,self.s))

    def toString(self):
        return "Time()"
