from observer import *
from GPS_Mediator import *

class GPS_Parser(Subscriber, Colleague):
    def __init__(self):
        raise NotImplementedError
    def parse_sentence(self):
        raise NotImplementedError



class GPS_NMEA_parser(GPS_Parser):
    def __init__(self, mediator, identity):
        self.nmea_sentence=""
        Subscriber.__init__(self, "Parser")
        Colleague.__init__(self,mediator, identity)
        
    def parse_rmc(self, sentence):
        rmc_token = sentence.split(',')

        #print(rmc_token)
    
    def checksum_validator(self, sentence):
        
        sentence = sentence.strip('\n')
        nmeadata,cksum = sentence.split('*', 1)
        nmeadata = nmeadata[1:]
        #print("nmeadata: {}".format(nmeadata) )
        #print("cksum: {}".format(cksum) )


        calc_cksum = 0
        for s in nmeadata:
            for i in s:
                calc_cksum ^= ord(i)

        cmp_val = hex(calc_cksum)[2:].upper()
        #print("calc_cksum: {}".format(cmp_val))

        if cmp_val.strip('\n') == cksum.strip('\n'):
            return True
        else:
            raise ValueError("GPS NMEA checksum fail")

    def parse(self, sentence):

        print("parser: {}".format(sentence))

        try:
            GPS_NMEA_parser.checksum_validator(self, sentence)
        except:
            return

        if "rmc" in sentence.lower():
            self.parse_rmc(sentence.lower())

        self._mediator.distribute(self, sentence)

    def send(self, message):
        print("Message '" + message + "' sent by Colleague " + str(self._id))
        self._mediator.distribute(self, message)
    
    def receive(self, message):
        print("Message '" + message + "' received by Colleague " + str(self._id))
