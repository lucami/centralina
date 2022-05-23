import calendar
import time
from Core.Logger.ApplicationLogger import Log

class Scheduler:
    def __init__(self, name):
        self.name = name
        self.task = {}
        self.time = calendar.timegm(time.gmtime())
        self.logger = Log()

    def add_task(self, kicker_obj, name=None):
        if name is None:
            name = kicker_obj
        #print("{} put in the scheduler - {}".format(name, kicker_obj))
        self.task.update({name: kicker_obj})

    def run(self):
        t = calendar.timegm(time.gmtime())
        if t - self.time >= 10:
            self.time = calendar.timegm(time.gmtime())
        else:
            #print("troppo presto")
            return

        for n, t in self.task.items():
            self.logger.debug("TaskSchedule.run - exec {}".format(n))
            t.kick()

    def remove_task(self, param):
        if param in self.task:
            del self.task[param]
            print("{} removed from scheduler".format(param))
        else:
            print("{} not found in the scheduler".format(param))


class Kicked:
    def __init__(self):
        self.delta_t = 0
        self.priority = 0
        self.avg_delta = 0
        self.last_exec = 0

    def kick(self):
        self.time_stats()
        pass

    def time_stats(self):
        now = (time.time())
        self.delta_t = round(now - self.last_exec)
        self.last_exec = now
        self.avg_delta = (self.avg_delta + self.delta_t) / 2
        #print(f"delta exec: {self.delta_t}")


if __name__ == "__main__":

    uno = Kicked()
    due = Kicked()
    scheduler = Scheduler("Main Scheduler")

    scheduler.add_task(uno, "uno")
    scheduler.add_task(due, "due")

    while True:
        scheduler.run()
        time.sleep(1)
