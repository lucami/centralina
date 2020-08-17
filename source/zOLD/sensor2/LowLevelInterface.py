import threading
import time
from zOLD.observer import *


class LowLevelInterface(threading.Thread, Publisher):
    def __init__(self):
        pass

    def run(self):
        pass


class NMEA_Interface(LowLevelInterface):
    def __init__(self, char_queue, packet_queue, threadID, name):
        self.char_queue = char_queue
        self.packet_queue = packet_queue
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.buffer = ''
        self.state = 0

    def run(self):
        # print("Running {}".format(self.name))
        self.buffer = ''
        self.state = 0
        while True:

            try:
                element = self.char_queue.get(block=False)
                self.char_queue.task_done()
                #print("element:{}".format(element))
                element = str(element, 'utf-8')
            except:
                time.sleep(1)
                continue

            if element == '$':
                self.state = 1
                continue
            elif '\n' in element:
                self.state = 0
                self.packet_queue.put(self.buffer)
                # print(self.buffer)
                self.buffer = ''
                continue

            if self.state == 1:
                self.buffer = self.buffer + element
