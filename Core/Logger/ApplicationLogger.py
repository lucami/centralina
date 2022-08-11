from datetime import datetime



class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Log(object):
    __metaclass__ = Singleton

    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    d = now.strftime("%Y-%m-%d")
    log = open(f"/home/debian/centralina/records/log_{t}_{d}.log", "w", buffering=1)

    def __init__(self):
        print("Log init")
        #logging.basicConfig(filename='AirQuality.log', level=logging.DEBUG)
        pass

    def debug(self, s):
        # logging.debug(s)
        self.log.write(f"DEBUG {datetime.now().strftime('%H:%M:%S')} {s}\n")
        #print(f"log: {s}")
        self.log.flush()

    def info(self, s):
        # logging.info(s)
        self.log.write(f"INFO {datetime.now().strftime('%H:%M:%S')} {s}\n")
        #print(f"log: {s}")
        self.log.flush()

    def warning(self, s):
        # logging.warning(s)
        self.log.write(f"WANRING {datetime.now().strftime('%H:%M:%S')} {s}\n")
        #print(f"log: {s}")
        self.log.flush()

    def error(self, s):
        # logging.error(s)
        self.log.write(f"ERROR {datetime.now().strftime('%H:%M:%S')} {s}\n")
        #print(f"log: {s}")
        self.log.flush()

if __name__ == "__main__":
    l1 = Log()
    l2 = Log()

    l1.debug("Sono l1")
    l2.debug("Sono l2")
    l1.warning("L1 warning")
    l2.error("L2 error")
