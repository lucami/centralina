import os
import subprocess
import time
from sysv_ipc import *


class Parser():
    def __init__(self):
        pass

    def parse(self):
        pass

    def kick(self):
        pass


class Bosh_Parser():
    def __init__(self):
        self.k = ftok("\\tmp\\", 65)
        self.m = MessageQueue(self.k)
        self.data = ''
        while True:
            try:
                self.data = self.m.receive(block=False)
                print(self.data)
            except:
                break

        pass

    def kick2(self):
        # print("Bosh_Parser kicked")
        self.parse2()

    def parse2(self):
        while True:
            try:
                last = self.m.receive(block=False)
                self.data = last
            except:
                break
        print("msg queue data: {}".format(self.data))



if __name__ == '__main__':
    pid = os.fork()
    if pid is 0:
        subprocess.call(['/home/debian/centralina/source/Bosh/bsp', '&'], shell=False)
    p = Bosh_Parser()
    while True:
        p.kick2()
        time.sleep(1)
