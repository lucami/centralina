from zOLD.observer import *
from zOLD.sensor_facade import *


class facade(Sensor_Facade, Subscriber):
    def __init__(self):
        Subscriber.__init__(self, "facade")
        self.time = 0
        self.date = 0
        self.latitude = 0
        self.longitude = 0
        self.quality = ""
        self.new_data = False
        self.f = open("/tmp/gpslog.txt", "w")
        self.i = 0

    def data_update(self, msg):
        # print("gps facade: {}".format(msg))
        s = msg.split(';')
        try:
            self.time = s[0]
            self.date = s[1]
            self.latitude = s[2]
            self.longitude = s[3]
            if "A" in s[4] and "1" in s[4]:
                self.quality = "good"
            else:
                self.quality = "bad"
            self.new_data = True
            self.i += 1
        finally:
            pass

    def get_time(self):
        self.new_data = False
        return self.time[0:2] + ":" + self.time[2:4] + ":" + self.time[4:6]

    def get_date(self):
        self.new_data = False
        return self.time

    def get_latitude(self):
        self.new_data = False
        return self.time

    def get_longitude(self):
        self.new_data = False
        return self.time

    def get_quality(self):
        self.new_data = False
        return self.quality

    def get_position(self):
        try:
            self.new_data = False
            # 4537.63300 N 00902.33694 E
            # 4916.45,N,12311.12,W
            # 49 + (16.45/60) = 49.2741 N
            # 123 + (11.12/60) = 123.1853 W
            a = self.latitude[0:2]
            # print(a)
            b = str(round(float(self.latitude[2:-2]) / 60, 5))[2:] + " " + self.latitude[-1]
            # print(b)
            lat = a + "." + b
            # print("{}.{}".format(a,b))

            a = self.longitude[0:3]
            # print(a)
            b = str(round(float(self.longitude[3:-2]) / 60, 5))[2:] + " " + self.longitude[-1]
            # print(b)
            # print("{}.{}".format(a,b))
            lon = a + "." + b
            # return str(self.latitude) + " " + str(self.longitude)
            return str(lat) + ";" + str(lon)
        except:
            return "0.0 N;0.0 W"

    def data_ready(self):
        return self.new_data

    def get_data(self):
        try:
            self.new_data = False
            return self.get_position() + ";" + self.get_time() + ";" + self.get_quality() + ";"
        except:
            return "not valid;"
