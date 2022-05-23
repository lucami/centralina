import time

from Core.Scheduler.TaskSchedule import Kicked
from Core.Sensor.Sensor import Sensor
from Core.Logger.ApplicationLogger import Log


class DigitalInSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.port = 1028
        self.msg = b'a'
        self.logger = Log()

    def kick(self):
        self.socket.sendto(self.msg, (self.ip, self.port))
        data = self.socket.recvfrom(1024)
        self.dispatch(data)
        Kicked.kick(self)


class DIDataManager:
    def __init__(self):
        self.state = ""
        pass

    def parse_data(self, sentence):
        s = sentence[0]
        s = bytes.decode(s)
        self.state = s
        #print(f"DI: {self.state}")


if __name__ == "__main__":
    s = DigitalInSensor()
    while True:
        s.kick()
        time.sleep(0.5)
