from LowLevelInterface import *
from Poll_Thread import *
from parser import *
import queue
from gps_data import *
from facade import *
sys.path.insert(0,'./sensor')
from scheduler import *
from kick import *


class gps_factory():
    def __init__(self, type):
        self.parser = None

        if "nmea" in type and "sim" in type:
            self.nmea_sim()
        elif "nmea" in type and "serial" in type:
            self.nmea_serial()
        else:
            print ("ERROR in running mode")

    def get_parser(self):
        return self.parser

    def get_facade(self):
        return self.fac

    def nmea_sim(self):
        q1 = queue.Queue()
        q2 = queue.Queue()

        poll = SerialNMEASim(q1,1, "Poll Thread")
        low = NMEA_Interface(q1, q2, 2, "Low Level interface Thread")
        parser = NMEA_Parser(q2)

        self.parser = parser

        gps_data_adapter = Gps_Data()
        parser.register(gps_data_adapter, gps_data_adapter.nmea_update)

        self.fac = facade()
        gps_data_adapter.register(self.fac, self.fac.gps_data_update)

        low.start()
        poll.start()

    def nmea_serial(self):
        q1 = queue.Queue()
        q2 = queue.Queue()

        poll = SerialPoll(q1,1, "Poll Thread")
        low = NMEA_Interface(q1, q2, 2, "Low Level interface Thread")
        parser = NMEA_Parser(q2)

        self.parser = parser

        gps_data_adapter = Gps_Data()
        parser.register(gps_data_adapter, gps_data_adapter.nmea_update)

        self.fac = facade()
        gps_data_adapter.register(self.fac, self.fac.gps_data_update)

        low.start()
        poll.start()
        pass
