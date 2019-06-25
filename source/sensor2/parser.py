from LowLevelInterface import *
from observer import *

class Parser(Subscriber):
    def __init__(self):
        pass
    def parse():
        pass

class NMEA_Parser(Parser):
    def __init__(self):
        self.rmc_sentence=""
        self.gga_sentence=""
        pass

    def parse(sentence):
        print(sentence)
        pass
    
    def crc_check(sentence):
        pass
    
    def deliver_rmc(sentence):
        pass
    
    def deliver_gga(sentence):
        pass

class JSON_Parser(Parser):
    def __init__(self):
        pass


