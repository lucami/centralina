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
        if "nmea" in type and "sim" in type:
            self.nmea_sim()
        elif "nmea" in type and "serial" in type:
            self.nmea_serial()

    def nmea_sim(self):


    def nmea_sim(self):
        pass


q1 = queue.Queue()
q2 = queue.Queue()

poll = SerialNMEASim(q1,1, "Poll Thread")
low = NMEA_Interface(q1, q2, 2, "Low Level interface Thread")
parser = NMEA_Parser(q2)

gps_data_adapter = Gps_Data()
parser.register(gps_data_adapter, gps_data_adapter.nmea_update)


facade = facade()
gps_data_adapter.register(facade, facade.gps_data_update)



low.start()
poll.start()

s = Scheduler("task scheduler")
s.add_task(parser, "parser")

while True:
    s.run()
