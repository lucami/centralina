import time

from Core.Scheduler.TaskSchedule import Kicked
from Core.Sensor.Sensor import Sensor


class PMSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.port = 1027
        self.msg = b'a'

    def kick(self):
        self.socket.sendto(self.msg, (self.ip, self.port))
        self.socket.recvfrom(1024)
        Kicked.kick(self)


if __name__ == "__main__":
    s = PMSensor()
    while True:
        s.kick()
        time.sleep(0.5)
