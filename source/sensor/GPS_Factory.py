import json # https://jsonlint.com
import configparser
from GPS_Communication import *
from GPS_Parser import * 
from latitude import *
from longitude import *
from observer import *

#urir-hlmp-gjrl-lowa
class GPSFactory():
    def __init__(self, gps_source):
        
        self.GPS_interfaces = {}

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
    
        self.gps_comm = None
        

        if "dummy" in self.mod_source and "nmea" in self.mod_source:
            #print("Creo istanza Dummy GPS")        
            self.gps_comm = GPS_Dummy_NMEA()
            a=self.gps_comm.toString()
        else:
            print("Non riesco a creare Dummy GPS")        
        
        self.GPS_interfaces.update({'GPS_Communication': self.gps_comm})
        return self.gps_comm

    def build_parser(self):
        self.parser = None
        
        if "nmea" in self.mod_source.lower():
            #print("Creo istanza Dummy Parser")        
            self.parser = GPS_NMEA_parser()
            self.rmc_parser = RMC_parser()
            self.gga_parser = GGA_parser()
        else:
            print("Non riesco a creare NMEA Parser")        
        
        self.GPS_interfaces.update({'parser': self.parser})

        return self.parser, self.rmc_parser, self.gga_parser

    def build_latitude(self):
        latitude = None
        latitude = Latitude()

        self.GPS_interfaces.update({'latitude': latitude})
        return latitude

    def build_longitude(self):
        longitude = None
        longitude = Longitude()
        
        self.GPS_interfaces.update({'longitude': longitude})

        return longitude

    def get_builds(self):
        return (self.GPS_interfaces)


def test_gps_factory():

    g=GPSFactory("TEST_NMEA")

    gps_device = g.build_gps()
    parser,rmc_parser, gga_parser=g.build_parser()
    latitude = g.build_latitude()
    longitude = g.build_longitude()   

    if gps_device is None:
        print("Dummy is None")

    gps_device.register(parser, parser.parse)
    
    parser.register(rmc_parser, rmc_parser.parse_rmc)
    parser.register(gga_parser, gga_parser.parse_gga)

    rmc_parser.register(latitude, latitude.set)
    rmc_parser.register(longitude, longitude.set)


    gps_device.get()
    gps_device.poll()

    gps_device.get()
    gps_device.poll()

    gps_device.get()
    gps_device.poll()

    gps_device.get()
    gps_device.poll()

test_gps_factory()


