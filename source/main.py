#!/usr/bin/env python
from daemons.prefab import run
import logging
from AirSensor.airsensor_factory import *
from Bosh.Bosh_Factory import *
from DataHandler.DataHandlerFactory import *
from fileManager.FileManager import *
from sensor2.gps_factory import *


class SleepyDaemon(run.RunDaemon):

    def run(self):
        file_manager = FileManager()
        print("file manager OK")
        g_factory = gps_factory("nmea serial")
        print("gps factory OK")
        gps_facade = g_factory.get_facade()
        print("gps facade OK")

        aq_factory = airsensor_factory()
        print("air sensor factory OK")
        aq_facade = aq_factory.get_facade()
        print("air sensor facade OK")

        bosh_factory = BoshFactory()
        print("bosh factory OK")
        bosh_facade = bosh_factory.get_facade()
        print("bosh facade OK")

        dh_factory = DataHandler_Factory()
        print("data handler factory OK")
        data_handler = dh_factory.get_data_handler()
        print("data handler factory OK")

        s = Scheduler("task scheduler")
        print("scheduler OK")

        data_handler.add_sensor("Air Sensor Facade", aq_facade)
        data_handler.add_sensor("GPS Facade", gps_facade)
        data_handler.add_sensor("Bosh Facade", bosh_facade)

        print("Data handler received sensors")

        s.add_task(g_factory.get_parser(), "gps parser")
        s.add_task(aq_factory.get_parser(), "air quality parser")
        s.add_task(bosh_factory.get_parser(), "bosh parser")
        s.add_task(data_handler, "Data Handler")

        print("Scheduler received tasks")

        data_handler.register(file_manager, file_manager.data_update)
        print("data handler register file manager")
        while True:
            s.run()


if __name__ == '__main__':

    print("run main")

    f = open("/home/debian/log2", "w")

    action = sys.argv[1]
    pidfile = "/tmp/main.pid"
    logfile = "/home/debian/main.log"

    print("set log")

    f.write("create daemon...")

    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    d = SleepyDaemon(pidfile=pidfile)

    f.write("created")

    if action == "start":
        print("Starting")
        f.write("Starting")
        d.start()

    elif action == "stop":
        print("Stopping")
        f.write("Stopping")
        d.stop()

    elif action == "restart":
        print("Restarting")
        f.write("Restarting")
        d.restart()
