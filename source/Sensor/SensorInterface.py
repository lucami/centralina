import time


class SensorInterface:
    def __init__(self, name, time_schedule):
        self.name = name
        self.time_poll = time_schedule
        self.last_time_poll = 0
        address = "127.0.0.1"
        self.port = 0

        if self.name is "GPS":
            self.port = 1026
        elif self.name is "htp":
            self.port = 1025
        elif self.name is "pm":
            self.port = 1027

    def get_name(self):
        return self.name

    def is_pollable(self):
        if time.time() - self.last_time_poll > self.time_poll:
            return True
        else:
            return False

    def take_data(self):
        self.last_time_poll = time.time()
        pass

    def get_header(self):
        pass

    def get_data(self):
        pass
