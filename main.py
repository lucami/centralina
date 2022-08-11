import time

from Core.Collector.DataCollector import DataCollector
from Core.DateTimeManager.SystemInterface import DateTimeInterface
from Core.Logger.ApplicationLogger import Log
from Core.Logger.RemoteLoggerinterface import RemoteLogger
from Core.Scheduler.TaskSchedule import Scheduler
from Core.Sensor.digital_in import DigitalInSensor
from Core.Sensor.gps import GPSSensor
from Core.Sensor.htp import HTPSensor
from Core.Sensor.pm import PMSensor
from datetime import datetime

if __name__ == "__main__":

    main_logger = Log()

    scheduler = Scheduler("MainScheduler")
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    d = now.strftime("%Y:%m:%d")
    main_logger.debug(f"Application INIT at {t} {d}")

    htp = HTPSensor()
    pm = PMSensor()
    gps = GPSSensor()
    di = DigitalInSensor()
    # rl = RemoteLogger()
    dc = DataCollector()
    dti = DateTimeInterface()

    main_logger.debug("Client Service Initiated")

    dti.register("DTI", dc.update)
    htp.register("HTP", dc.update)
    pm.register("PM", dc.update)
    gps.register("GPS", dc.update)
    di.register("DI", dc.update)

    scheduler.add_task(dti)
    scheduler.add_task(htp)
    scheduler.add_task(pm)
    scheduler.add_task(gps)
    scheduler.add_task(di)
    scheduler.add_task(dc)

    #scheduler.add_task(rl)

    while True:
        scheduler.run()
        time.sleep(0.5)
