import time
from WiFiManager.WiFi_Interface import WLanOn, WLanOff


class GPIO46Manager:
    def __init__(self):
        self.gpio_file = open("/sys/class/gpio/gpio46/value", "r")
        self.old_state = self.gpio_file.read(4).strip()
        self.gpio_file.seek(0, 0)
        self.f = open("/tmp/status.txt", "w")
        self.f.write("START: {}".format(self.old_state))

    def run(self):
        self.manage_changes()
        while True:
            state = self.gpio_file.read(4).strip()
            self.gpio_file.seek(0, 0)

            if state not in self.old_state:
                self.old_state = state
                self.manage_changes()

            self.old_state = state

            '''
            if state not in self.old_state:
                self.old_state = state
                self.manage_changes()
            '''
            time.sleep(10)

    def manage_changes(self):
        if '1' in self.old_state:
            self.f.write("STATO: 1")
            on = WLanOn()
            on.run()
        elif '0' in self.old_state:
            self.f.write("STATO: 0")
            off = WLanOff()
            off.run()
        self.f.flush()

    def switch_on_AP(self):
        pass

    def switch_on_client(self):
        pass

    def switch_off(self):
        pass
