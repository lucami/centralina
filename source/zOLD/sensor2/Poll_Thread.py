import random
import threading
import time
import serial


class PollThread(threading.Thread):
    def __init__(self):
        pass

    def run(self):
        pass

    def get_id(self):
        pass

    def get_name(self):
        pass

    def get_queue(self):
        pass


class SerialPoll(PollThread):
    def __init__(self, chracter_queue, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.char_queue = chracter_queue
        self.port = serial.Serial('/dev/ttyS4')
        #self.f = open("/tmp/gpslog.txt", "w")
        pass

    def run(self):
        # print("Running {}".format(self.name))
        while True:
            car = self.port.read()
            self.char_queue.put(car)
            #self.f.write("{}".format(str(car, 'utf-8')))
            #self.f.flush()
        pass

    def get_id(self):
        return self.threadID

    def get_name(self):
        return self.name

    def get_queue(self):
        return self.char_queue


class SerialNMEASim(PollThread):
    def __init__(self, chracter_queue, threadID, name, shotdown_event):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.char_queue = chracter_queue
        self.dataset = "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A\r\n" \
                       "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47\r\n"
        self.shotdown_event = shotdown_event

        pass

    def run(self):
        print("Running {}".format(self.name))
        while True:
            if self.shotdown_event.is_set(timeout=None):
                break
            time_to_sleep = random.randint(0, 100)
            positive = random.randint(0, 1)
            if positive:
                time.sleep(1 + time_to_sleep / 1000)
            else:
                time.sleep(1 - time_to_sleep / 1000)

            for i in self.dataset:
                self.char_queue.put(i)
                time_to_sleep = random.randint(0, 10)
                time.sleep(time_to_sleep / 10000)
        pass

    def get_id(self):
        return self.threadID

    def get_name(self):
        return self.name

    def get_queue(self):
        return self.char_queue
