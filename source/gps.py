import sys
sys.path.insert(0,'./sensor')
from GPS_Factory import *

#test_gps_factory()
factory = gps_factory("TEST_NMEA")
print (factory.GPS_interfaces)


