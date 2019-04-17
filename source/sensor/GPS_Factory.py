import json # https://jsonlint.com
import configparser
from GPS_Communication import *

class GPSFactory():
    def __init__(self, gps_source):
        
        self.mod_source=""
        self.mod_format=""

        with open('gps_conf.json', 'r') as f:
            config = json.load(f)

        if gps_source == "DEFAULT":
            self.mod_source = config['DEFAULT']['SOURCE']
            self.mod_format = config['DEFAULT']['FORMAT']
            #print ("GPS CONF: default") 

        if gps_source == "TEST_NMEA":
            self.mod_source = config['TEST_NMEA']['SOURCE']
            self.mod_format = config['TEST_NMEA']['FORMAT']
            #print ("GPS CONF: test nmea") 

        if gps_source == "TEST_JSON":
            self.mod_source = config['TEST_JSON']['SOURCE']
            self.mod_format = config['TEST_JSON']['FORMAT']
            #print ("GPS CONF: test json")
        
    def build_gps(self):
        dummy_nmea = None
        if "dummy" in self.mod_source and "nmea" in self.mod_source:
            #print("Creo istanza Dummy GPS")        
            dummy_nmea = GPS_Dummy_NMEA()
            a=dummy_nmea.toString()
        else:
            print("Non riesco a creare Dummy GPS")        
        return dummy_nmea

def test_gps_factory():

    g=GPSFactory("TEST_NMEA")
    dummy = g.build_gps()

    if dummy is None:
        print("Dummy is None")

    dummy.toString()
    s =dummy.get()
    print (s) 
    dummy.poll()

    s =dummy.get()
    print (s) 
    dummy.poll()

    s =dummy.get()
    print (s) 
    dummy.poll()

test_gps_factory()
