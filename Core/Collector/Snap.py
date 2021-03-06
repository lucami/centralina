from BSP.system_time.system_time import get_current_time
from Core.Dispatcher.Dispatch import Subscriber
from Core.Logger.ApplicationLogger import Log


class Snapshot:
    def __init__(self):
        self.gps_data = ""
        self.htp_data = ""
        self.pm_data = ""
        self.di_data = ""
        self.file_size = 0
        self.file = ""
        self.logger = Log()
        self.time_date = ""

    def clean_snap(self):
        self.gps_data = ""
        self.htp_data = ""
        self.pm_data = ""
        self.di_data = ""

    def load_time_date(self, data):
        self.time_date = data
        print(f"Snap: {self.time_date}")
        pass

    def load_gps_data(self, data):
        self.gps_data = data
        pass

    def load_pm_data(self, data):
        self.pm_data = data
        pass

    def load_htp_data(self, data):
        self.htp_data = data
        pass

    def load_di_data(self, data):
        pass

    def take_snap(self):
        sentence = f"{self.gps_data} {self.htp_data} {self.pm_data}"

        if self.file_size == 0:
            self.open_file()

        self.write_file(sentence)
        self.logger.debug("Snap.take_snap")

        # print(f"SNAP: {sentence}")



    def write_file(self, s):
        self.file.write(s + '\n')
        self.file_size += len(s) + 1

        if self.file_size > 15360:
            self.close_file()
            self.file_size = 0

    def close_file(self):
        self.file.close()

    def open_file(self):
        self.file = open("/home/debian/centralina/records/record_" + self.time_date + ".csv", "w", buffering=1)
