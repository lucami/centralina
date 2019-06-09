import sys
import time
sys.path.insert(0,'./sensor')
from GPS_Factory import *
from scheduler import *
from kick import *
from GPS_Facade import *
from opt_manager import parser

p=parser()

if p.get_gps_arg() == 'fake':
    facade = GPS_Facade("TEST_NMEA")
else:
    facade = GPS_Facade("DEFAULT")

s = Scheduler("task scheduler")


s.add_task(facade, "facade")

if p.get_scheduler_arg() == 'test':
    dummy = kicker()
    s.add_task(dummy, "Dummy")

i=0
while True:
    i=i+1
    time.sleep(2)
    s.run()
    print(facade.get_position())
    print(facade.get_time_date())
    print(facade.get_validity())
    if i == 4 and p.get_scheduler_arg() == 'test':
        s.remove_task("Dummy")
    if i == 7 and p.get_scheduler_arg() == 'test':
        s.add_task(dummy, "Dummy")
    print("")
