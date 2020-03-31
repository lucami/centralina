from sensor2.singleton import *
from observer import *


class Airsensor_Data(Singleton, Subscriber, Publisher):

    def __init__(self):
        Subscriber.__init__(self, "Gps_Data")
        Publisher.__init__(self)
        self.pm10 = 0
        self.pm2p5 = 0
        self.checksum_ok = "1"

    def air_data_update(self, msg):
        # print("AirSensor data receiver: {}".format(msg))
        self.pm10 = split = msg.split(';')[0]
        self.pm2p5 = split = msg.split(';')[1]
        self.checksum_ok = "1"
        # print("AirSensor data receiver: {} - {} - {}".format(type(self.pm10), type(self.pm2p5), type(self.checksum_ok)))
        self.deliver()
        pass

    def deliver(self):
        str_to_publish = self.pm10 + ";" + self.pm2p5 + ";" + self.checksum_ok
        # print("dispatch: {}".format(str_to_publish))
        Publisher.dispatch(self, str_to_publish)
