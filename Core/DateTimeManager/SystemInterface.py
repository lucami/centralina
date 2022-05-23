import time
from datetime import datetime

from Core.Dispatcher.Dispatch import Publisher
from Core.Scheduler.TaskSchedule import Kicked


class DateTimeInterface(Kicked, Publisher):
    def __init__(self):
        Kicked.__init__(self)
        Publisher.__init__(self)
        self.date = ""
        self.time = ""
        self.time_source = "local"

    def kick(self):
        self.set_time()
        self.dispatch(self.get_time())

    def get_time(self):
        return self.date + "_" + self.time

    def set_time(self):
        if self.time_source in "local":
            self.set_time_date_from_local()
        else:
            self.set_time_date_from_gps()

    def set_time_date_from_local(self):
        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")
        self.date = now.strftime("%Y:%m:%d")

    def set_time_date_from_gps(self):
        pass


if __name__ == "__main__":
    dti = DateTimeInterface()
    print(dti.get_time())
    dti.kick()
    print(dti.get_time())
    time.sleep(2)
    dti.kick()
    print(dti.get_time())
