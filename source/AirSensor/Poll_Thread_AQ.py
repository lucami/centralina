import threading
import time
import serial
import queue
import random
import time

class PollThread_AQ(threading.Thread):
    def __init__(self):
        pass
    def run(self):
        pass
    def get_id(self):
        pass
    def get_name(self):
        pass
    def get_queue(self):
        pass


class SerialPoll_AQ(PollThread_AQ):
    def __init__(self, chracter_queue, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.char_queue = chracter_queue
        self.port = serial.Serial('/dev/ttyS0',baudrate=9600,timeout=1)
        packet = bytearray()

        packet.append(0x68)
        packet.append(0x01)
        packet.append(0x02)
        packet.append(0x95)
        #send stop
        self.port.write(packet)
        a=self.port.read(4)
        '''print(len(a))
        for i in range(len(a)):
            print(a[i])'''
        time.sleep(2)


        packet.append(0x68)
        packet.append(0x01)
        packet.append(0x40)
        packet.append(0x57)
        #set to autosend
        self.port.write(packet)
        a=self.port.read(4)
        '''print(len(a))
        for i in range(len(a)):
            print(a[i])'''

        packet = bytearray()
        packet.append(0x68)
        packet.append(0x01)
        packet.append(0x01)
        packet.append(0x96)
        #set to autosend
        self.port.write(packet)
        a=self.port.read(4)
        '''print(len(a))
        for i in range(len(a)):
            print(a[i])'''
        pass

    def run(self):

        while True:
            car = self.port.read()
            #print("Poll_Thread_AQ: {}".format(car))
            self.char_queue.put(car)
        pass

    def get_id(self):
        return self.threadID

    def get_name(self):
        return self.name

    def get_queue(self):
        return self.char_queue

class SerialAirSim(PollThread_AQ):
    def __init__(self, chracter_queue, threadID, name):

        pass

    def run(self):
        pass

    def get_id(self):
        return self.threadID

    def get_name(self):
        return self.name

    def get_queue(self):
        return self.char_queue
