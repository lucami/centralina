from observer import *
from kick import *
import calendar
import time

class FileManager(Publisher):
    def __init__(self):
        self.filename="data_"+str(calendar.timegm(time.gmtime()))+".log"
        self.log_file = open(self.filename, "w", buffering=-1)
        self.file_size=0
        pass

    def data_update(self, msg):
        #print("FileManager: {}".format(msg))

        self.log_file.write(msg+";"+"\r\n")
        self.file_size+=len(msg+";"+"\r\n")

        if self.file_size >= 1024:
            self.log_file.close()
            self.file_size=0
            self.filename="data_"+str(calendar.timegm(time.gmtime()))+".log"
            self.log_file = open(self.filename, "w", buffering=-1)

    def close_file(self):
        self.log_file.close()
