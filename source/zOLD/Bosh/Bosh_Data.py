from zOLD.sensor2.singleton import *
from zOLD.observer import *


class Bosh_Data(Singleton, Subscriber, Publisher):

    def __init__(self):
        Subscriber.__init__(self, "Bosh_Data")
        Publisher.__init__(self)
        self.humidity = 0
        self.pressure = 0
        self.temperature = 0

    def bosh_update(self, msg):
        #print("Bosh_Data receiver: {}".format(msg))
        msg_splitted = msg.split(',')
        self.temperature = msg_splitted[0]
        self.humidity = msg_splitted[1]
        self.pressure = msg_splitted[2]

        #print("DEBUG        {} | {} | {}".format(self.temperature, self.pressure, self.humidity))

        self.deliver()

    def deliver(self):
        # str_to_publish = self.time +";"+self.date+";"+self.latitude+";"+self.longitude+";"+self.quality
        str_to_publish = self.temperature + ";" + self.humidity + ";" + self.pressure + ";"
        #print("bosh_update: {}".format(str_to_publish))
        Publisher.dispatch(self, str_to_publish)
