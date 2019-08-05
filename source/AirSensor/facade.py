from observer import *

class facade(Subscriber):
    def __init__(self):
        Subscriber.__init__(self, "facade")
        self.pm10 = 0
        self.pm2p5  = 0
        self.crc_ok  = 0


    def air_data_update(self, msg):
        #print("facade: {}".format(msg))
        s=msg.split(';')
        self.pm10 = s[0]
        self.pm2p5 = s[1]
        self.crc_ok = s[2]
        self.new_data=1

    def get_pm10(self):
        self.new_data=0
        return self.pm10

    def get_pm2p5(self):
        self.new_data=0
        return self.pm2p5

    def get_crc_ok(self):
        self.new_data=0
        return self.crc_ok

    def new_airsensor_data(self):
        return self.new_data

    def get_air_data(self):
        self.new_data=0
        return self.pm10+";"+self.pm2p5+";"+self.crc_ok
