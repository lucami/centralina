from source.Sensor.SensorInterface import *


class SensorGPS(SensorInterface):
    def __init__(self, name, time_schedule):
        super().__init__(name, time_schedule)
        self.time = "0"
        self.position = "0"
        self.quality = "0"

    def take_data(self):
        pass

    def get_header(self):
        return "time; position; quality;"

    def get_data(self):
        return self.time + ";" + self.position + ";" + self.quality + ";"


if __name__ == "__main__":
    s = SensorGPS("a", 1)
    print(s.get_name())
