from singleton import *
from observer import *

class Gps_Data(Singleton, Subscriber, Publisher):

    def __init__(self):
        Subscriber.__init__(self, "Gps_Data")
        Publisher.__init__(self)
        self.time = 0
        self.date  = 0
        self.latitude  = 0
        self.longitude  = 0
        self.quality  = 0

    def nmea_update(self, msg):
        #print("Gps_Data receiver: {}".format(msg))
        rmc = split=msg.split(';')[0]
        gga = split=msg.split(';')[1]

        checkval=True

        checkval &= self.check_time(rmc)
        checkval &= self.check_date(rmc)
        checkval &= self.check_lat(rmc)
        checkval &= self.check_lon(rmc)
        checkval &= self.check_quality(rmc,gga)

        if not checkval:
            self.time = 0
            self.date  = 0
            self.latitude  = 0
            self.longitude  = 0
            self.quality  = 0
        else:
            self.deliver()
        pass

    def check_time(self, rmc):
        self.time=str(rmc.split(',')[1])
        #print("time: {}".format(time))
        return True

    def check_date(self,rmc):
        self.date=str(rmc.split(',')[9])
        #print("date: {}".format(date))
        return True

    def check_lat(self,rmc):
        self.lat=str(rmc.split(',')[3])
        self.lat+=" "+str(rmc.split(',')[4])
        #print("lat: {}:{}".format(lat))
        return True

    def check_lon(self,rmc):
        self.lon=str(rmc.split(',')[5])
        self.lon += " " +str(rmc.split(',')[6])
        #print("lon: {}:{}".format(lon))
        return True

    def check_quality(self,rmc,gga):
        self.quality=str(rmc.split(',')[2])
        self.quality += ":"+str(gga.split(',')[6])
        #print("quality: {}:{}".format(q))
        return True

    def deliver(self):
        #str_to_publish = self.time +";"+self.date+";"+self.latitude+";"+self.longitude+";"+self.quality
        str_to_publish = self.time +";"+self.date+";"+self.lat+";"+self.lon+";"+self.quality+";"
        #print("dispatch: {}".format(str_to_publish))
        Publisher.dispatch(self, str_to_publish)


    def set_time(self):
        pass
    def set_date(self):
        pass
    def set_latitude(self):
        pass
    def set_longitude(self):
        pass
    def set_quality(self):
        pass

    def get_time(self):
        pass
    def get_date(self):
        pass
    def get_latitude(self):
        pass
    def get_longitude(self):
            pass
    def get_quality(self):
        pass
