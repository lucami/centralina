from LowLevelInterface import *
from Poll_Thread import *
from parser import *
import queue
from airsensor_data import *
from facade import *
sys.path.insert(0,'./sensor')
from scheduler import *
from kick import *


class airsensor_factory():
    def __init__(self):
        self.parser = None
        self.airquality_serial()

    def get_parser(self):
        return self.parser

    def get_facade(self):
        return self.fac

    def airquality_serial(self):
        q1 = queue.Queue()
        q2 = queue.Queue()

        poll = SerialPoll(q1,1, "Poll Thread")
        low = Honeywell_Interface(q1, q2, 2, "Low Level interface Thread")
        parser = HONEYWELL_Parser(q2)

        self.parser = parser

        airquality_data_adapter = Airsensor_Data()
        parser.register(airquality_data_adapter, airquality_data_adapter.air_data_update)

        self.fac = facade()
        airquality_data_adapter.register(self.fac, self.fac.air_data_update)

        low.start()
        poll.start()
        pass
