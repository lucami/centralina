from zOLD.observer import *
from zOLD.sensor_facade import *


class Bosh_Facade(Sensor_Facade, Subscriber):
    def __init__(self):
        Subscriber.__init__(self, "Bosh_Facade")
        self.humidity = 0
        self.temperature = 0
        self.pressure = 0
        self.new_data = False

    def data_update(self, msg):
        #print("Bosh_Facade update: {}".format(msg))
        s = msg.split(';')
        try:
            self.temperature = (s[0])[3:]
            self.humidity = s[1]
            self.pressure = s[2].split('\\')[0]
            self.new_data = True
            #print("{} - {} - {}".format(self.get_temperature(), self.get_humidity(), self.get_pressure()))
        finally:
            pass

    def get_temperature(self):
        self.new_data = False
        return self.temperature

    def get_humidity(self):
        self.new_data = False
        return self.humidity

    def get_pressure(self):
        self.new_data = False
        return self.pressure

    def data_ready(self):
        return self.new_data

    def get_data(self):
        self.new_data = False
        return str(self.get_temperature() + ";" + self.get_humidity() + ";" + self.get_pressure() + ";")
