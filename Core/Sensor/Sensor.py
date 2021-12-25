import socket
from Core.Dispatcher.Dispatch import Publisher
from Core.Scheduler.TaskSchedule import Kicked


class Sensor (Kicked, Publisher):
    ip = "127.0.0.1"
    socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    def __init__(self):
        Kicked.__init__(self)
        Publisher.__init__(self)
        pass

