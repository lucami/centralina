import time


class GPIO46Manager:
    def __init__(self):
        self.gpio_file = open("/sys/class/gpio/gpio46/value", "r")
        self.old_state = self.gpio_file.read(4).strip()
        self.gpio_file.seek(0, 0)
        self.f = open("/tmp/status.txt", "w")
        self.f.write("START: {}".format(self.old_state))

    def get_status(self):
        state = self.gpio_file.read(4).strip()
        self.gpio_file.seek(0, 0)
        new_state = "old"
        if state != self.old_state:
            self.old_state = state
            new_state = "new"

        return state, new_state


if __name__ == "__main__":
    switch = GPIO46Manager()

    while True:
        status, trigger = switch.get_status()
        print("{} {}".format(status, trigger))
        time.sleep(3)
