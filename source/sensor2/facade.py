from observer import *

class facade(Subscriber):
    def __init__(self):
        Subscriber.__init__(self, "facade")
        self.time = 0
        self.date  = 0
        self.latitude  = 0
        self.longitude  = 0
        self.quality  = 0


    def gps_data_update(self, msg):
        print("gps_data_update")
        print("facade: {}".format(msg))
