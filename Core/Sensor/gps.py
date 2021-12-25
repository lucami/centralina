import time

from Core.Scheduler.TaskSchedule import Kicked
from Core.Sensor.Sensor import Sensor


class GPSSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.port = 1026
        self.msg = b'a'

    def kick(self):
        self.socket.sendto(self.msg, (self.ip, self.port))
        self.socket.recvfrom(1024)
        Kicked.kick(self)


if __name__ == "__main__":
    s = GPSSensor()
    while True:
        s.kick()
        time.sleep(0.5)
