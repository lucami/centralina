import threading
import time
import serial
import queue
import random
import time

class PollThread(threading.Thread):
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


class SerialPoll(PollThread):
    def __init__(self, chracter_queue, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.char_queue = chracter_queue
        self.port = serial.Serial('/dev/ttyS0',baudrate=9600,timeout=1)

        packet = bytearray()
        packet.append(0x68)
        packet.append(0x01)
        packet.append(0x40)
        packet.append(0x57)
        #set to autosend
        self.port.write(packet)
        self.port.read(4)

        packet = bytearray()
        packet.append(0x68)
        packet.append(0x01)
        packet.append(0x01)
        packet.append(0x96)
        #set to autosend
        self.port.write(packet)
        self.port.read(4)

        pass

    def run(self):

        while True:
            char = self.port.read()
            self.char_queue.put(char)
        pass

    def get_id(self):
        return self.threadID

    def get_name(self):
        return self.name

    def get_queue(self):
        return self.char_queue

class SerialAirSim(PollThread):
    def __init__(self, chracter_queue, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.char_queue = chracter_queue
        self.dataset = "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A\r\n"\
        "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47\r\n"
        pass

    def run(self):
        pass

    def get_id(self):
        return self.threadID

    def get_name(self):
        return self.name

    def get_queue(self):
        return self.char_queue
