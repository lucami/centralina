import signal

from AirSensor.airsensor_factory import *
from Bosh.Bosh_Factory import *
from DataHandler.DataHandlerFactory import *
from fileManager.FileManager import *
from sensor2.gps_factory import *

file_manager = FileManager()


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    file_manager.close_file()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

g_factory = gps_factory("nmea serial")
gps_facade = g_factory.get_facade()

aq_factory = airsensor_factory()
aq_facade = aq_factory.get_facade()

bosh_factory = BoshFactory()
bosh_facade = bosh_factory.get_facade()

dh_factory = DataHandler_Factory()
data_handler = dh_factory.get_data_handler()

s = Scheduler("task scheduler")

data_handler.add_sensor("Air Sensor Facade", aq_facade)
data_handler.add_sensor("GPS Facade", gps_facade)
data_handler.add_sensor("Bosh Facade", bosh_facade)

s.add_task(g_factory.get_parser(), "gps parser")
s.add_task(aq_factory.get_parser(), "air quality parser")
s.add_task(bosh_factory.get_parser(), "bosh parser")
s.add_task(data_handler, "Data Handler")

data_handler.register(file_manager, file_manager.data_update)

i = 0
while True:
    s.run()
