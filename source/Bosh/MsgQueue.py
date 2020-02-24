from sysv_ipc import *


class MsgQueue:
    def __init__(self):
        self.k = ftok("\\tmp\\", 65)
        self.m = MessageQueue(self.k)

    def poll(self):
        a = self.m.receive()
        print(a)


if __name__ == '__main__':
    msg_queue = MsgQueue()
    while True:
        msg_queue.poll()
