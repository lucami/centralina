import time

from Core.Collector.Snap import Snapshot
from Core.Dispatcher.Dispatch import Subscriber
from Core.Scheduler.TaskSchedule import Kicked, Scheduler
from Core.Sensor.digital_in import DigitalInSensor, DIDataManager
from Core.Sensor.gps import GPSSensor, GPSDataManager
from Core.Sensor.htp import HTPSensor, HTPDataManager
from Core.Sensor.pm import PMSensor, PMDataManager


class DataCollector(Kicked, Subscriber):

    def __init__(self):
        Kicked.__init__(self)
        Subscriber.__init__(self, "DataCollector")
        self.gps_data_manager = GPSDataManager()
        self.htp_data_manager = HTPDataManager()
        self.pm_data_manager = PMDataManager()
        self.di_data_manager = DIDataManager()
        self.snap = Snapshot()
        pass

    def kick(self):
        self.snap.load_gps_data(self.gps_data_manager.get_data())
        self.snap.load_htp_data(self.htp_data_manager.get_data())
        self.snap.load_pm_data(self.pm_data_manager.get_data())
        self.snap.take_snap()
        self.snap.clean_snap()

    def update(self, message, subscriber_name):
        if "GPS" in subscriber_name:
            self.gps_data_manager.parse_data(message)
        elif "HTP" in subscriber_name:
            self.htp_data_manager.parse_data(message)
        elif "PM" in subscriber_name:
            self.pm_data_manager.parse_data(message)
        elif "DI" in subscriber_name:
            self.di_data_manager.parse_data(message)
        else:
            print('{} ricevuto messaggio "{} da {}'.format(self.name, message, subscriber_name))


if __name__ == "__main__":

    scheduler = Scheduler("MainScheduler")

    htp = HTPSensor()
    pm = PMSensor()
    gps = GPSSensor()
    di = DigitalInSensor()

    dc = DataCollector()

    htp.register("HTP", dc.update)
    pm.register("PM", dc.update)
    gps.register("GPS", dc.update)
    di.register("DI", dc.update)

    scheduler.add_task(htp)
    scheduler.add_task(pm)
    scheduler.add_task(gps)
    scheduler.add_task(di)
    scheduler.add_task(dc)

    while True:
        scheduler.run()
        time.sleep(0.5)
