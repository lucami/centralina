from observer import *
import sys
import threading
import time

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





class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"
def main():
    for x in range(4):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, invoke the run method
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another




class GPS_Serial(GPS_Communication):
    def __init__(self):
        self.dev = None
        self.addr = "/dev/ttyS4"
        self.error=0
        Publisher.__init__(self)
        kicker.__init__(self)
        SerialListener.__init__(self)

        self.dev = open(self.addr, "r")
        
        #try:

        #except:

    def toString(self):
        str_ = "GPS_Serial"
        #print (str_)
        return str_

    def execute(self):

        '''

        leggi una riga finche non ha:
            piu niente da leggere
            NMEA unknown error

            salva riga nell array n

        metti l'arrei nella coda

        :return:
        '''

        #leggi tutte le righe
        #for per ogni riga
        #   dispatch per ogni riga
        sentences = []
        sentece=""
        again=0

        while True:
            sentence = self.dev.readline()
            if 'NMEA unknown msg' in sentence:
                break

        while True:
            print(">{}<".format(sentence))
            sentences.append(sentence)
            sentence = self.dev.readline()
            if "RMC" in sentence:
                   break

        #if "RMC" in self.sentence:
        #    self.sentence = self.gga_sentence
        #else:
        #    self.sentence = self.rmc_sentence

        Publisher.dispatch(self, sentences)


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
        #self.rmc_sentence = "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A"
        Publisher.__init__(self)
        kicker.__init__(self)
        self.sentences = [] 
        #self.sentences.append("GPRMC,,V,,,,,,,,,,N*53")
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
        '''for i in self.sentences:
            print(i)
        '''
        Publisher.dispatch(self, self.sentences)

class GPS_Dummy_JSON(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass
