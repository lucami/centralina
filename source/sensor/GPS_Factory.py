import json # https://jsonlint.com
import configparser
from GPS_Dummy import *

class GPSFactory():
    def __init__(self, gps_source):
        
        with open('gps_conf.json', 'r') as f:
            config = json.load(f)

        if gps_source == "DEFAULT":
            gps_source = config['DEFAULT']['SOURCE']
            gps_format = config['DEFAULT']['FORMAT']
            print ("GPS CONF: default") 

        if gps_source == "TEST_NMEA":
            gps_source = config['TEST_NMEA']['SOURCE']
            gps_format = config['TEST_NMEA']['FORMAT']
            print ("GPS CONF: test nmea") 

        if gps_source == "TEST_JSON":
            gps_source = config['TEST_JSON']['SOURCE']
            gps_format = config['TEST_JSON']['FORMAT']
            print ("GPS CONF: test json")



g=GPSFactory("TEST_JSON")




