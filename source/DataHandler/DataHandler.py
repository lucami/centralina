import sys
import os

sys.path.insert(0, '../')
from sensor_facade import *
from kick import *
from observer import *
import collections


class Data_Handler(kicker, Publisher):
    def __init__(self):
        Publisher.__init__(self)
        self.sensor = collections.OrderedDict()
        self.datafromsensor = ""
        self.counter = 0

    def add_sensor(self, name, obj):
        self.sensor.update({name: obj})
        # print("{} added to data handler".format(name))
        # print("Sensor list: \r\n")
        # for n,t in self.sensor.items():
        #   print("->{}".format(n))

    def remove_sensor(self, check_name):
        if check_name in self.sensor:
            del self.sensor[check_name]

    def kick(self):
        self.read_data()

    def read_data(self):
        # print("read data")
        a = True
        for n, t in self.sensor.items():
            #print("{} data ready: {}".format(n, t.data_ready()))
            a &= t.data_ready()
        if a:
            #print("data ready!")
            #os.system('clear')
            for n, t in self.sensor.items():
                #print("{} #### {}".format(type(t), n))
                a = t.get_data()
                #print("n: {}".format(n, a))
                self.datafromsensor += a
                #print("datafromsensor: {}".format(self.datafromsensor))
            self.deliver()
        else:
            self.counter += 1
            if self.counter >= 5:
                self.datafromsensor = "NO DATA AVAILABLE"
                self.counter = 0
            #print("{}".format(self.datafromsensor + ";"))
            # self.log_file.write("\r\n")
            self.deliver()
            #print(self.datafromsensor)

    def deliver(self):
        Publisher.dispatch(self, self.datafromsensor)
        self.datafromsensor = ""
