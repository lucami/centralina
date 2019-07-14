import sys
sys.path.insert(0,'./sensor2')

from factory import *
from scheduler import *


f=factory("nmea sim")
gps_facade = f.get_facade()

s = Scheduler("task scheduler")
s.add_task(f.get_parser(), "parser")

while True:
    s.run()

    print(gps_facade.get_position())
