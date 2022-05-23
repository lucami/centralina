import logging


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Log(object):
    __metaclass__ = Singleton

    def __init__(self):
        # logging.basicConfig(filename='AirQuality.log', level=logging.DEBUG)
        self.log = open("AirQuality.log", "w", buffering=1)

    def debug(self, s):
        # logging.debug(s)
        self.log.write(f"DEBUG {s}")

    def info(self, s):
        # logging.info(s)
        self.log.write(f"INFO {s}")

    def warning(self, s):
        # logging.warning(s)
        self.log.write(f"WANRING {s}")

    def error(self, s):
        # logging.error(s)
        self.log.write(f"ERROR {s}")


if __name__ == "__main__":
    l1 = Log()
    l2 = Log()

    l1.debug("Sono l1")
    l2.debug("Sono l2")
    l1.warning("L1 warning")
    l2.error("L2 error")
