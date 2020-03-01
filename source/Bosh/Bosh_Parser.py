from observer import *
import sys
from sysv_ipc import *

sys.path.insert(0, '../')
from kick import *


class Parser(Publisher, kicker):
    def __init__(self):
        pass

    def parse(self):
        pass

    def kick(self):
        pass


class Bosh_Parser(Parser):
    def __init__(self):
        Publisher.__init__(self)
        self.k = ftok("\\tmp\\", 65)
        self.m = MessageQueue(self.k)
        self.data = ''
        try:
            self.m.receive()
        except:
            pass

        pass

    def kick(self):
        # print("Bosh_Parser kicked")
        self.parse()

    def parse(self):
        try:
            self.data = self.m.receive()
            #print("msg queue data: {}".format(self.data))
        except:
            pass#print("msg queue except")

        try:
            self.deliver()
        except:
            pass#print("deliver except")

    def deliver(self):
        str_to_publish = str(self.data)
        Publisher.dispatch(self, str_to_publish)
        #print("msg queue publisher: {}".format(self.data))
