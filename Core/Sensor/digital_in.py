import time

from Core.Scheduler.TaskSchedule import Kicked
from Core.Sensor.Sensor import Sensor


class DigitalInSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.port = 1028
        self.msg = b'a'

    def kick(self):
        self.socket.sendto(self.msg, (self.ip, self.port))
        data = self.socket.recvfrom(1024)
        self.dispatch(data)
        Kicked.kick(self)


if __name__ == "__main__":
    s = DigitalInSensor()
    while True:
        s.kick()
        time.sleep(0.5)
