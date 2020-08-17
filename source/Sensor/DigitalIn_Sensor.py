from source.Sensor.SensorInterface import *


class SensorDigitalIn(SensorInterface):
    def __init__(self, name, time_schedule):
        super().__init__(name, time_schedule)
        self.stato="0"
        self.name = name
        self.time_schedule = time_schedule

    def take_data(self):
        pass

    def get_header(self):
        return "stato;"

    def get_data(self):
        return self.stato+";"
