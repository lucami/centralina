import sys
import os
sys.path.insert(0,'./sensor2')

from factory import *
from scheduler import *


f=factory("nmea serial")
gps_facade = f.get_facade()

s = Scheduler("task scheduler")
s.add_task(f.get_parser(), "parser")
while True:
    s.run()

    if gps_facade.new_gps_data() == 1:
        os.system('clear')
        print("{}".format(gps_facade.get_time()))
        print("{}".format(gps_facade.get_position()))
        print("{}".format(gps_facade.get_quality()))
