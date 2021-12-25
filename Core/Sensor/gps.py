import time

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


# b'$GPRMC,173500.00,A,4137.39254,N,01320.01658,E,0.718,,251221,,,A*7B\n,A*6E\n$GPGGA,173500.00,4137.39254,N,01320.01658,E,1,05,1.49,184.7,M,42.5,M,,*5E\n$GPVTG,,T,,M,0.718,N,1.330,K,A*2C\n,A*38\n$GPGSA,A,3,32,29,24,12,02,,,,,,,,3.54,1.49,3.22*02\n5\n', ('127.0.0.1', 1026)) da GPS"
class GPSDataManager:
    def __init__(self):
        self.time = ""
        self.nord = ""
        self.est = ""

    def parse_data(self, sentence):
        rmc = sentence[0]
        rmc = bytes.decode(rmc)
        print(f"{type(rmc)} {len(rmc)} {rmc}")

if __name__ == "__main__":
    s = GPSSensor()
    while True:
        s.kick()
        time.sleep(0.5)
