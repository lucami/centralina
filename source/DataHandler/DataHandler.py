import os
sys.path.insert(0,'../')
from sensor_facade import *
from kick import *

class Data_Handler(kick):
    def __init__(self):
        self.sensors = {}

    def add_sensor(self, name, obj):
        self.sensor.update({name: obj})

    def remove_sensor(self, check_name):
        if check_name in self.sensor:
            del self.sensor[check_name]

    def read_data(self):
        a = True
        for n,t in self.sensors.items():
            a &= t.data_ready()
        if a:
            print("data ready!")
            for n,t in self.sensors.items():
                print(t.get_data())
        else:
            print("not all data ready!")
