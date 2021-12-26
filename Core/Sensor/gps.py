import time

from BSP.system_time.system_time import set_current_time
from Core.Scheduler.TaskSchedule import Kicked
from Core.Sensor.Sensor import Sensor


class GPSSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.port = 1026
        self.msg = b'a'

    def kick(self):
        self.socket.sendto(self.msg, (self.ip, self.port))
        data = self.socket.recvfrom(1024)
        self.dispatch(data)
        Kicked.kick(self)


class GPSDataManager:
    def __init__(self):
        self.time = ""
        self.nord = ""
        self.est = ""
        self.valid = ""
        self.date = ""

    def parse_date(self, raw_date):
        return raw_date[0:2] + "-" + raw_date[2:4] + "-" + raw_date[4:6]

    def parse_time(self, raw_time):
        return raw_time[0:2] + ":" + raw_time[2:4] + ":" + raw_time[4:6]

    def parse_nord(self, raw_nord):
        s = ""
        try:
            s = str(float(raw_nord[0:2]) + float(raw_nord[2:]) / 60)
        finally:
            return s

    def parse_est(self, raw_est):
        s = ""
        try:
            s = str(float(raw_est[0:3]) + float(raw_est[3:]) / 60)
        finally:
            return s

    def rmc_parse(self, rmc_s):
        rmc_s = rmc_s.split(',')
        self.date = self.parse_date(rmc_s[9])
        self.time = self.parse_time(rmc_s[1])
        self.valid = rmc_s[2]
        self.nord = self.parse_nord(rmc_s[3])
        self.est = self.parse_est(rmc_s[5])

    def parse_data(self, sentence):
        s = sentence[0]
        s = bytes.decode(s)
        s = s.split()
        for i in s:
            if "RMC" in i:
                self.rmc_parse(i)
                '''
                print(f"time: {self.time}")
                print(f"valid: {self.valid}")
                print(f"nord: {self.nord}")
                print(f"est: {self.est}")
                '''

    def get_data(self):
        return self.date + ";" + self.time + ";" + self.valid + ";" + self.nord + ";" + self.est + ";"

    def get_header(self):
        return "date;time;valid;nord;est;"


if __name__ == "__main__":
    s = GPSSensor()
    while True:
        s.kick()
        time.sleep(0.5)
