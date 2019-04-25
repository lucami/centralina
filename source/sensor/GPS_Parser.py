class GPS_Parser():
    def __init__(self):
        raise NotImplementedError
    def parse_sentence(self):
        raise NotImplementedError

class GPS_NMEA_parser(GPS_Parser):
    def __init__(self, lat, lon):
        self.nmea_sentence=""
        self.latitude = lat
        self.longitude = lon
        lat.toString()
        
    def parse_rmc(self, sentence):
        rmc_token = sentence.split(',')
        self.latitude.set(rmc_token[3])
        self.longitude.set(rmc_token[5])
        #print(rmc_token)
    
    def parse(self, sentence):
        if "rmc" in sentence.lower():
            self.parse_rmc(sentence.lower())
