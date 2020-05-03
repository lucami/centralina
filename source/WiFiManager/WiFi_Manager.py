from HW_Status_Monitor import GPIO46Manager
from kick import kicker


class WiFiManager(kicker):
    def __init__(self):
        self.hw_status_monitor
        self.switch = GPIO46Manager()
