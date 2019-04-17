import json # https://jsonlint.com
import configparser
from GPS_Dummy import *

class GPSFactory():
    def __init__(self, gps_source):
        
        self.mod_source=""
        self.mod_format=""

        with open('gps_conf.json', 'r') as f:
            config = json.load(f)

        if gps_source == "DEFAULT":
            mod_source = config['DEFAULT']['SOURCE']
            mod_format = config['DEFAULT']['FORMAT']
            print ("GPS CONF: default") 

        if gps_source == "TEST_NMEA":
            mod_source = config['TEST_NMEA']['SOURCE']
            mod_format = config['TEST_NMEA']['FORMAT']
            print ("GPS CONF: test nmea") 

        if gps_source == "TEST_JSON":
            mod_source = config['TEST_JSON']['SOURCE']
            mod_format = config['TEST_JSON']['FORMAT']
            print ("GPS CONF: test json")
        
    def build_gps(self):
        
        if "dummy" in self.mod_source and "NMEA" in self.mod_source:
            dummy_nmea = GPS_Dummy_NMEA()
            return dummy_nmea
    

g=GPSFactory("TEST_NMEA")
dummy = g.build_gps()

s =dummy.get()
print (s) 
dummy.poll()

s =dummy.get()
print (s) 
dummy.poll()

s =dummy.get()
print (s) 
dummy.poll()


