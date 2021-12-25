import time

from Core.Dispatcher.Dispatch import Subscriber
from Core.Scheduler.TaskSchedule import Kicked, Scheduler
from Core.Sensor.digital_in import DigitalInSensor
from Core.Sensor.gps import GPSSensor, GPSDataManager
from Core.Sensor.htp import HTPSensor
from Core.Sensor.pm import PMSensor


class DataCollector(Kicked, Subscriber):

    def __init__(self):
        Kicked.__init__(self)
        Subscriber.__init__(self, "DataCollector")
        self.gps_data_manager = GPSDataManager()

        pass

    def add_sensor(self, sensor):
        pass

    def kick(self):
        print("DataCollector Kick")

    def update(self, message, subscriber_name):
        if "GPS" in subscriber_name:
            self.gps_data_manager.parse_data(message)
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
