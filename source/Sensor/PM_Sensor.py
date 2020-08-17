from source.Sensor.SensorInterface import *


class SensorPM(SensorInterface):
    def __init__(self, name, time_schedule):
        super().__init__(name, time_schedule)
        self.pm10 = "0"
        self.pm2p5 = "0"

    def take_data(self):
        pass

    def get_header(self):
        return "pm10; pm2p5;"

    def get_data(self):
        return self.pm10+";"+self.pm2p5+";"


pm = SensorPM("PM", 1)

print(pm.get_header())
