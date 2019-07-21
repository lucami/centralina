from LowLevelInterface import *
from observer import *
import sys
sys.path.insert(0,'../')
from kick import *

class Parser(Publisher, kicker):
    def __init__(self):
        pass

    def parse(self):
        pass

    def kick(self):
        pass

class NMEA_Parser(Parser):
    def __init__(self, sentence_queue):
        Publisher.__init__(self)
        self.rmc=""
        self.gga=""
        self.sentence_queue=sentence_queue
        pass

    def kick(self):
        self.parse()

    def checksum_check(self, sentence):
        sentence = sentence.strip('\n')

        try:
            nmeadata,cksum = sentence.split('*', 1)
        except:
            return False

        calc_cksum = 0
        for s in nmeadata:
            for i in s:
                calc_cksum ^= ord(i)

        cmp_val = hex(calc_cksum)[2:].upper()

        if cmp_val in cksum:
            return True
        else:
            return False
        pass


    def parse(self):
        sentence = self.sentence_queue.get(block=1)
        self.sentence_queue.task_done()
        self.checksum_check(sentence)
        rval = True
        if self.checksum_check(sentence):
            pass
            #print("Estratta {}".format(sentence))
        else:
            rval=False
            print("checksum error")

        if "RMC" in sentence and rval == True:
            self.rmc=sentence
            self.gga=""
        elif "GGA" in sentence and rval == True:
            self.gga=sentence
            self.deliver()
            self.rmc=""
            self.gga=""

    def deliver(self):
        str_to_publish=self.rmc.strip("\r\n")+";"+self.gga.strip("\r\n")
        Publisher.dispatch(self, str_to_publish)
        #print("dispatch: {}".format(str_to_publish))

class JSON_Parser(Parser):
    def __init__(self):
        pass
