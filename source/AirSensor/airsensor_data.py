from singleton import *
from observer import *

class Airsensor_Data(Singleton, Subscriber, Publisher):

    def __init__(self):
        Subscriber.__init__(self, "Gps_Data")
        Publisher.__init__(self)
        self.pm10 = 0
        self.pm2p5  = 0
        self.checksum_ok  = 0

    def air_data_update(self, msg):
        #print("Gps_Data receiver: {}".format(msg))
        self.pm10 = split=msg.split(';')[0]
        self.pm2p5 = split=msg.split(';')[1]
        self.checksum_ok=0

        self.deliver()
        pass

    def deliver(self):
        #str_to_publish = self.time +";"+self.date+";"+self.latitude+";"+self.longitude+";"+self.quality
        str_to_publish = self.pm10 +";"+self.pm2p5+";"+self.checksum_ok
        #print("dispatch: {}".format(str_to_publish))
        Publisher.dispatch(self, str_to_publish)
