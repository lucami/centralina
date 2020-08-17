from zOLD.observer import *
import sys
from sysv_ipc import *

sys.path.insert(0, '../')
from zOLD.kick import *


class Parser(Publisher, kicker):
    def __init__(self):
        pass

    def parse(self):
        pass

    def kick(self):
        pass


class Bosh_Parser(Parser):
    def __init__(self):
        print("Bosh parser init...")
        Publisher.__init__(self)
        self.k = ftok("\\tmp\\", 65)
        self.m = MessageQueue(self.k)
        self.data = ''
        while True:
            try:
                last = self.m.receive(block=False)
                self.data = last
                print("Bosh parser init OK")
            except:
                print("Bosh parser init ERROR")
                break

        pass

    def kick(self):
        # print("Bosh_Parser kicked")
        self.parse()

    def parse(self):
        while True:
            try:
                last = self.m.receive(block=False)
                self.data = last
            except:
                break
        try:
            self.deliver()
        except:
            pass  # print("deliver except")

    def deliver(self):
        str_to_publish = str(self.data)
        Publisher.dispatch(self, str_to_publish)
        print("msg queue publisher: {}".format(self.data))
