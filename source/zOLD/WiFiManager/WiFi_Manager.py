from zOLD.HW_Status_Monitor import GPIO46Manager
from zOLD.kick import kicker
from zOLD.WiFiManager.WiFi_Interface import *


class WiFiManager(kicker):
    def __init__(self):
        self.switch = GPIO46Manager()
        self.wlan_on = WLanOn()
        self.wlan_off = WLanOff()

    def kick(self):
        status, trigger = self.switch.get_status()
        if "new" in trigger:
            if '1' in status:
                self.wlan_on.run()

            else:
                self.wlan_off.run()
