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

class HONEYWELL_Parser(Parser):
    def __init__(self, sentence_queue):
        Publisher.__init__(self)
        self.pm10=""
        self.pm2p5=""
        self.sentence_queue=sentence_queue
        pass

    def kick(self):
        self.parse()




    def parse(self):
        sentence = self.sentence_queue.get(block=1)
        self.sentence_queue.task_done()
        rval = True

        self.pm10 = sentence[6]+sentence[7]
        self.pm2p5 = sentence[8]+sentence[9]

    def deliver(self):
        str_to_publish=self.pm10.strip("\r\n")+";"+self.pm2p5.strip("\r\n")
        Publisher.dispatch(self, str_to_publish)
        #print("dispatch: {}".format(str_to_publish))

class JSON_Parser(Parser):
    def __init__(self):
        pass
