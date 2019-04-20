class GPS_Parser():
    def __init__(self):
        raise NotImplementedError
    def parse_sentence(self):
        raise NotImplementedError

class GPS_NMEA_parser(GPS_Parser):
    def __init__(self):
        self.nmea_sentence=""
    
    def parse_rmc(self, sentence):
        rmc_token = sentence.split(',')
        print(rmc_token)
    
    def parse(self, sentence):
        if "rmc" in sentence.lower():
            self.parse_rmc(sentence.lower())

