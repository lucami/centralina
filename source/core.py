import sys
import os
from scheduler import *

sys.path.insert(0,'./sensor2')
from gps_factory import *

sys.path.insert(0,'./AirSensor')
from airsensor_factory import *


g_factory=gps_factory("nmea simulator")
gps_facade = g_factory.get_facade()

aq_factory=airsensor_factory()
aq_facade = aq_factory.get_facade()

s = Scheduler("task scheduler")
s.add_task(g_factory.get_parser(), "gps parser")
s.add_task(aq_factory.get_parser(), "air quality parser")

while True:
    s.run()

    if gps_facade.new_gps_data() == 1 and aq_facade.new_airsensor_data()==1:
        os.system('clear')
        print("{}".format(gps_facade.get_time()))
        print("{}".format(gps_facade.get_position()))
        print("{}".format(gps_facade.get_quality()))
        print("{}".format(aq_facade.get_air_data()))
