import time
from Core.Logger.ApplicationLogger import Log
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


class HTPDataManager:
    def __init__(self):
        self.temperature = ""
        self.pressure = ""
        self.humidity = ""
        self.log= Log()
        pass

    def parse_data(self, sentence):
        # print(f"sentence: {sentence}")
        s = sentence[0]
        s = bytes.decode(s)
        s = s.split(";")
        try:
            self.temperature = s[0]
            self.humidity = s[1]
            self.pressure = s[2]
        except:
            self.temperature = "-100"
            self.humidity = "-100"
            self.pressure = "-100"
            self.log.error(f"HTP Sensor parsing error. Received: {s}")



        # print(f"T: {self.temperature} H: {self.humidity} P: {self.pressure}")

    def get_data(self):
        return self.temperature + ";" + self.pressure + ";" + self.humidity + ";"

    def get_header(self):
        return "temperature;pressure;humidity;"


if __name__ == "__main__":
    s = HTPSensor()
    while True:
        s.kick()
        time.sleep(0.5)
