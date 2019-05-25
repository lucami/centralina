import sys
import time
sys.path.insert(0,'./sensor')
from GPS_Factory import *
from scheduler import *
from kick import *
from GPS_Facade import *


s = Scheduler("task scheduler")
facade = GPS_Facade("TEST_NMEA")
dummy = kicker()

s.add_task(facade, "facade")
s.add_task(dummy, "Dummy")
i=0
while True:
    i=i+1
    time.sleep(2)
    s.run()
    print(facade.get_position())
    print(facade.get_time_date())
    print(facade.get_validity())
    if i == 4:
        s.remove_task("Dummy")
    if i == 7:
        s.add_task(dummy, "Dummy")
    print("")
