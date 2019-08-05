from observer import *
import re

class GPS_Parser(Subscriber, Publisher): 
    def __init__(self):
        raise NotImplementedError
    def parse_sentence(self):
        raise NotImplementedError



class GPS_NMEA_parser(GPS_Parser):
    def __init__(self):
        self.nmea_sentence=""
        Subscriber.__init__(self, "Parser")
        Publisher.__init__(self)
        


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

    def parse(self, sentences):


        for s in sentences:
            print("--> {} <--".format(s))

        for s in sentences:
            try:
              GPS_NMEA_parser.checksum_validator(self, s)

            except:
                print("checksum fail")
                pass

            Publisher.dispatch(self, s)
'''
$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A

     RMC          Recommended Minimum sentence C
     123519       Fix taken at 12:35:19 UTC
     A            Status A=active or V=Void.
     4807.038,N   Latitude 48 deg 07.038' N
     01131.000,E  Longitude 11 deg 31.000' E
     022.4        Speed over the ground in knots
     084.4        Track angle in degrees True
     230394       Date - 23rd of March 1994
     003.1,W      Magnetic Variation
     *6A          The checksum data, always begins with *
'''
class RMC_parser(Publisher, Subscriber):

    def __init__(self):
        Publisher.__init__(self)
        Subscriber.__init__(self, "RMC_parser")
        self.rmc_sentence = ""
        self.time_position = 1
        self.coordinate_regex = '\A\d{3,5}\.\d{2,3}'

    def parse_rmc(self, sentence):

        if "RMC" in sentence:

            if self.check_all(sentence) is True:
                #split = sentence.split(',')
                #print ("{} - {}".format(len(split), split))

                Publisher.dispatch(self, sentence)
        

    def check_all(self, sentence):
        check_val = True
        check_val &= self.check_gprmc(sentence)
        check_val &= self.check_time(sentence)
        check_val &= self.check_date(sentence)
        check_val &= self.check_status(sentence)
        check_val &= self.check_lat(sentence)
        check_val &= self.check_lon(sentence)
        check_val &= self.check_speed(sentence)
        check_val &= self.check_angle(sentence)
        check_val &= self.check_mag_var(sentence)
        return check_val

    def check_gprmc(self, sentence):
        
        if "RMC" in sentence:
            rval = True
        else:
            rval = False
        return rval
        
    def check_time(self, sentence):
        rval = True

        split=sentence.split(',')
        time =  split[1]
        
        if len(time) != 6:
            rval = False

        h = int(time[:2])
        m = int(time[2:4])
        s = int(time[4:6])
        
        if h < 0 and h > 24:
            rval = False
        if m < 0 and m > 60:
            rval = False
        if s < 0 and s > 60:
            rval = False
        return rval

    def check_date(self, sentence):
        rval = True

        split=sentence.split(',')
        date =  split[9]

        if len(date) != 6:
            rval = False

        g = int(date[0:2])
        m = int(date[2:4])
        a = int(date[4:6])
        
        if g < 1 and g > 31:
            rval = False
        if m < 1 and m > 12:
            rval = False
        if a < 0 and a > 99:
            rval = False

        return rval

    def check_status(self, sentence):
        rval = True
        split=sentence.split(',')
        flag =  split[2]
        direction = split[4]
        
        if 'A' in flag:
            rval = True
        else:
            rval = False
        return rval

    def check_lat(self, sentence):
        rval = True
        split=sentence.split(',')
        lat =  split[3]
        direction = split[4]

        if re.fullmatch(self.coordinate_regex, lat) == None and ( direction is 'N' or direction is 'S'):
            rval = False
        else:
            rval = True
        return rval
        
    def check_lon(self, sentence):
        rval = True
        split=sentence.split(',')
        lat =  split[5]
        direction = split[6]

        if re.fullmatch(self.coordinate_regex, lat) == None and ( direction is 'E' or direction is 'W'):
            rval = False
        else:
            rval = True
        return rval

    def check_speed(self, sentence):
        return True
    def check_angle(self, sentence):
        return True
    def check_mag_var(self, sentence):
        return True


class GGA_parser(Publisher, Subscriber):

    def __init__(self):
        Publisher.__init__(self)
        Subscriber.__init__(self, "GGA_parser")
        self.rmc_sentence = ""

    def parse_gga(self, sentence):
        if "GGA" in sentence:
            #print("parse_gga")
            Publisher.dispatch(self, sentence)
        pass

