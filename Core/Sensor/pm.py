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
        data = self.socket.recvfrom(1024)
        self.dispatch(data)
        Kicked.kick(self)


class PMDataManager:
    def __init__(self):
        self.pm10 = ""
        self.pm2p5 = ""
        pass

    def parse_data(self, sentence):
        s = sentence[0]
        s = bytes.decode(s)
        s = s.split(";")
        self.pm2p5 = s[0]
        self.pm10 = s[1]
        #print(f"pm2p5: {self.pm2p5} pm10:{self.pm10}")

    def get_data(self):
        return self.pm2p5 + ";" + self.pm10 + ";"

    def get_header(self):
        return "pm2p5;pm10;"


if __name__ == "__main__":
    s = PMSensor()
    while True:
        s.kick()
        time.sleep(0.5)
