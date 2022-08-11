import socket

import time
from Core.Sensor.Sensor import Sensor
from Core.Logger.ApplicationLogger import Log


class RemoteLogger(Sensor):
    def __init__(self):
        super().__init__()
        self.port = 1029
        self.msg = b''
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.s.setblocking(0)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.ip, self.port))
        self.logger = Log()

    def kick(self):
        try:
            data = self.s.recvfrom(1024)
            print(f"MSG: {data}")
            self.logger.debug(f"REMOTE LOG: {data}")
        except:
            pass


if __name__ == "__main__":
    rl = RemoteLogger()
    while True:
        rl.kick()
        time.sleep(0.5)
