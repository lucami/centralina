from zOLD.observer import *
import sys

sys.path.insert(0, '../')
from zOLD.kick import *


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
        self.pm10 = ""
        self.pm2p5 = ""
        self.sentence_queue = sentence_queue
        pass

    def kick(self):
        self.parse()

    def parse(self):
        try:
            sentence = self.sentence_queue.get(block=False)
            self.sentence_queue.task_done()
            # print("parser_AQ pre parse: {}".format(sentence))
            # print("Values: {}{} | {}{}".format(sentence[4],sentence[5],sentence[6],sentence[7]))
            rval = True

            pm2p5_1 = int.from_bytes(sentence[5], byteorder='big')
            pm2p5_2 = int.from_bytes(sentence[4], byteorder='big') << 8

            pm10_1 = int.from_bytes(sentence[7], byteorder='big')
            pm10_2 = int.from_bytes(sentence[6], byteorder='big') << 8

            self.pm10 = pm10_1 + pm10_2
            self.pm2p5 = pm2p5_1 + pm2p5_2

            # print("pm10: {}".format(self.pm10))
            # print("pm2.5: {}".format(self.pm2p5))
            self.deliver()
        except:
            pass

    def deliver(self):
        str_to_publish = str(self.pm10).strip("\r\n") + ";" + str(self.pm2p5).strip("\r\n")
        # print("parser_AQ: {}".format(str_to_publish))
        Publisher.dispatch(self, str_to_publish)


class JSON_Parser(Parser):
    def __init__(self):
        pass
