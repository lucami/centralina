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
        #print("facade: {}".format(msg))
        s=msg.split(';')
        self.time = s[0]
        self.date = s[1]
        self.latitude=s[2]
        self.longitude=s[3]
        if "A" in s[4] and "1" in s[4]:
            self.quality="good"
        else:
            self.quality="bad"

    def get_time(self):
        return self.time

    def get_date(self):
        return self.time

    def get_latitude(self):
        return self.time

    def get_longitude(self):
        return self.time

    def get_quality(self):
        return self.time

    def get_position(self):
        return str(self.latitude) + " " + str(self.longitude)
