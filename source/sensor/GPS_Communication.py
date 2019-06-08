from observer import *
import sys
sys.path.insert(0,'../')
from kick import *

class GPS_Communication(Publisher):
    def __init__(self):
        #inizializzazione parametri di Publisher
        

        raise NotImplementedError
     
    def poll(self):
        raise NotImplementedError
    
    def get(self):
        raise NotImplementedError

class GPS_Serial(GPS_Communication):
    def __init__(self):
        self.dev = None
        self.addr = "/dev/ttyS4"
        self.error=0
        Publisher.__init__(self)
        kicker.__init__(self)

        self.dev = open(self.addr, "r")
        
        #try:

        #except:

    def toString(self):
        str_ = "GPS_Serial"
        #print (str_)
        return str_

    def execute(self):
        #leggi tutte le righe
        #for per ogni riga
        #   dispatch per ogni riga
        sentence = self.dev.readline()
        print(">{}<".format(sentence))
        #if "RMC" in self.sentence:
        #    self.sentence = self.gga_sentence
        #else:
        #    self.sentence = self.rmc_sentence

        Publisher.dispatch(self, sentence)


class GPS_SPI(GPS_Communication):
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
        self.rmc_sentence ="GPRMC,,V,,,,,,,,,,N*53"
        #self.rmc_sentence = "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A"
        self.gga_sentence="$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
        self.sentence=self.rmc_sentence
        Publisher.__init__(self)
        kicker.__init__(self)
        self.sentences = [] 
        self.sentences.append("GPRMC,,V,,,,,,,,,,N*53")
        self.sentences.append("$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47")
        self.sentences.append("$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A")
        self.index = 0
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

    def execute(self):
        if self.index == 3:
            self.index = 0
        Publisher.dispatch(self, self.sentences[self.index])
        self.index = self.index+1; 

class GPS_Dummy_JSON(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass
