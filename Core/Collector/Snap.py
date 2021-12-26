from BSP.system_time.system_time import get_current_time


class Snapshot:
    def __init__(self):
        self.gps_data = ""
        self.htp_data = ""
        self.pm_data = ""
        self.di_data = ""

    def clean_snap(self):
        self.gps_data = ""
        self.htp_data = ""
        self.pm_data = ""
        self.di_data = ""

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
        print(f"SNAP: {self.gps_data} {self.htp_data} {self.pm_data}")
        pass
