from observer import *

class GPS_Communication(Publisher):
    def __init__(self):
        raise NotImplementedError 
    
    def poll(self):
        raise NotImplementedError
    
    def get(self):
        raise NotImplementedError

class GPS_SPI(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass

class GPS_Serial(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass

class GPS_Daemon(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass

class GPS_Dummy_NMEA(GPS_Communication):
    
    def __init__(self):
        #print ("DUMMY NMEA Generator built!")
        self.rmc_sentence = "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A"
        self.gga_sentence="$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
        self.sentence=self.rmc_sentence

        #inizializzazione parametri di Publisher
        Publisher.__init__(self)
        pass

    def toString(self):
        str_ = "GPS_Dummy_NMEA"
        #print (str_)
        return str_
        

    def poll(self):
        if "RMC" in self.sentence:
            self.sentence = self.gga_sentence
        else:
            self.sentence = self.rmc_sentence
    
    def get(self):

        Publisher.dispatch(self, self.sentence)

        

class GPS_Dummy_JSON(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass
