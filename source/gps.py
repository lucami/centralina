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

while True:
	time.sleep(2)
	s.run()
	print(facade.get_position())
	print(facade.get_time_date())
	print(facade.get_validity())
	print("")