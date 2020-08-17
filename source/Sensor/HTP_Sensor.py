from source.Sensor.SensorInterface import *


class SensorHTP(SensorInterface):
    def __init__(self, name, time_schedule):
        super().__init__(name, time_schedule)
        self.humidity = 0
        self.temperature = 0
        self.pressure = 0

    def take_data(self):
        pass

    def get_header(self):
        return "humidity; temperature; pressure;"

    def get_data(self):
        return self.pm10 + ";" + self.pm2p5 + ";"


htp = SensorHTP("HTP", 1)

print(htp.get_header())
