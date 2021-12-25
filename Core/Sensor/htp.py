import time

from Core.Scheduler.TaskSchedule import Kicked
from Core.Sensor.Sensor import Sensor


class HTPSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.port = 1025
        self.msg = b'a'

    def kick(self):
        self.socket.sendto(self.msg, (self.ip, self.port))
        data = self.socket.recvfrom(1024)
        self.dispatch(data)
        Kicked.kick(self)


if __name__ == "__main__":
    s = HTPSensor()
    while True:
        s.kick()
        time.sleep(0.5)
