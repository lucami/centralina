from observer import *
from sensor_facade import *

class facade_AQ(Sensor_Facade,Subscriber):
    def __init__(self):
        Subscriber.__init__(self, "facade")
        self.pm10 = 0
        self.pm2p5  = 0
        self.crc_ok  = 0
        self.new_data=False


    def data_update(self, msg):
        print("facade_AQ: {}".format(msg))
        s=msg.split(';')
        self.pm10 = s[0]
        self.pm2p5 = s[1]
        self.crc_ok = s[2]
        self.new_data=True

    def get_pm10(self):
        self.new_data=False
        return self.pm10

    def get_pm2p5(self):
        self.new_data=False
        return self.pm2p5

    def get_crc_ok(self):
        self.new_data=False
        return self.crc_ok

    def data_ready(self):
        return self.new_data

    def get_data(self):
        self.new_data=False
        return str(self.pm10)+";"+str(self.pm2p5)+";"+str(self.crc_ok)
