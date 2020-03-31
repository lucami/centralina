from observer import *
from kick import *
import calendar
import time


class FileManager(Publisher):
    def __init__(self):
        self.file_size = 6
        self.filename = ""
        self.open_file()

    def data_update(self, msg):
        # print("FileManager: {}".format(msg))
        self.log_file.write(msg + "\r\n")
        self.file_size += len(msg + "\r\n")
        self.log_file.flush()

        if self.file_size >= 2048:
            self.close_file()
            self.open_file()

    def close_file(self):
        self.log_file.write("END\n")
        self.log_file.close()

    def open_file(self):
        self.file_size = 0
        self.filename = "/home/debian/data_" + str(calendar.timegm(time.gmtime())) + ".log"
        self.log_file = open(self.filename, "w")
        self.log_file.write("OPEN\n")
        self.log_file.flush()
