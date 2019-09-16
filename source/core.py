import sys
import os
from scheduler import *
import calendar
import time
import signal
from threading import *



sys.path.insert(0,'./sensor2')
from gps_factory import *

sys.path.insert(0,'./AirSensor')
from airsensor_factory import *

sys.path.insert(0,'./DataHandler')
from DataHandlerFactory import *

sys.path.insert(0,'./fileManager')
from FileManager import *

file_manager = FileManager()


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    file_manager.close_file()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

g_factory=gps_factory("nmea serial")
gps_facade = g_factory.get_facade()


aq_factory=airsensor_factory()
aq_facade = aq_factory.get_facade()

dh_factory = DataHandler_Factory()
data_handler = dh_factory.get_data_handler()

s = Scheduler("task scheduler")

data_handler.add_sensor("Air Sensor Facade", aq_facade)
data_handler.add_sensor("GPS Facade", gps_facade)

s.add_task(g_factory.get_parser(), "gps parser")
s.add_task(aq_factory.get_parser(), "air quality parser")
s.add_task(data_handler, "Data Handler")

data_handler.register(file_manager, file_manager.data_update)

i=0
while True:
    s.run()
