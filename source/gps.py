import sys
sys.path.insert(0,'./sensor')
from GPS_Factory import *

#test_gps_factory()
factory = gps_factory("TEST_NMEA")

com = factory.GPS_interfaces['GPS_Communication']


com.kick()


