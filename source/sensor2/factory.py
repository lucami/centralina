from LowLevelInterface import *
from Poll_Thread import *
from parser import *
import queue
sys.path.insert(0,'./sensor')
from scheduler import *
from kick import *
from gps_data import *
from facade import *

class factory():
    def __init__(self, type):
        self.parser = None

        if "nmea" in type and "sim" in type:
            self.nmea_sim()
        elif "nmea" in type and "serial" in type:
            self.nmea_serial()

    def get_parser(self):
        return self.parser


    def nmea_sim(self):
        q1 = queue.Queue()
        q2 = queue.Queue()

        poll = SerialNMEASim(q1,1, "Poll Thread")
        low = NMEA_Interface(q1, q2, 2, "Low Level interface Thread")
        parser = NMEA_Parser(q2)

        self.parser = parser

        gps_data_adapter = Gps_Data()
        parser.register(gps_data_adapter, gps_data_adapter.nmea_update)

        f = facade()
        gps_data_adapter.register(f, f.gps_data_update)

        low.start()
        poll.start()

    def nmea_serial(self):
        pass

f=factory("nmea sim")
parser = f.get_parser()

s = Scheduler("task scheduler")
s.add_task(parser, "parser")

while True:
    s.run()
