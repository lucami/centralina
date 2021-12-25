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
        logging.basicConfig(filename='AirQuality.log', encoding='utf-8', level=logging.DEBUG)

    def debug(self, s):
        logging.debug(s)

    def info(self, s):
        logging.info(s)

    def warning(self, s):
        logging.warning(s)

    def error(self, s):
        logging.error(s)


if __name__ == "__main__":
    l1 = Log()
    l2 = Log()

    l1.debug("Sono l1")
    l2.debug("Sono l2")
    l1.warning("L1 warning")
    l2.error("L2 error")
