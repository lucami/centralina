import threading
from zOLD.observer import *


class LowLevelInterface(threading.Thread, Publisher):
    def __init__(self):
        pass
    def run(self):
        pass

class Honeywell_Interface(LowLevelInterface):
    def __init__(self, char_queue, packet_queue, threadID, name):
        self.char_queue = char_queue
        self. packet_queue = packet_queue
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.mark=0
        self.count = 0

    def run(self):
        #print("Running {}".format(self.name))
        self.buffer = []
        self.state = 0

        while True:
            try:
                element = self.char_queue.get(block=False)
                self.char_queue.task_done()
                #print("Honeywell_Interface element: {}".format(element))

                if self.mark == 0 and element == b'B':
                    self.mark = 1
                elif self.mark == 1 and element == b'M':
                    self.mark = 2
                elif self.mark == 2:
                    self.count = self.count+1

                    self.buffer.append(element)

                    if self.count == 29:
                        self.mark = 0
                        self.count = 0
                        self.packet_queue.put(self.buffer)
                        #print("Honeywell_Interface buffer: {}".format(self.buffer))
                        self.buffer= []
            except:
                pass

        '''
        while True:
            while True:
                try:
                    element = self.char_queue.get(block=False)
                    self.char_queue.task_done()
                    print("Honeywell_Interface: {}".format(element))
                    if element == b'B':
                        #pass
                        self.buffer.append(element)
                        break
                except:
                    pass
            while True:
                try:
                    element = self.char_queue.get(block=False)
                    self.char_queue.task_done()
                    self.buffer.append(element)

                    if element == b'\r':
                        print("Honeywell_Interface: {}".format(self.buffer))
                        self.buffer.append(element)
                        self.packet_queue.put(self.buffer)
                        self.buffer = []
                        break
                except:
                    pass


        '''
