from kick import *
import calendar
import time

class Scheduler():
    def __init__(self, name):
        self.name = name
        self.task = {}
        self.time = calendar.timegm(time.gmtime())

    def add_task(self, kicker, name = None):
        if name == None:
            name = kicker
        print("{} put in the scheduler".format(name))
        self.task.update({name: kicker})

    def run(self):


        t=calendar.timegm(time.gmtime())
        if t-self.time >= 10:
            self.time = calendar.timegm(time.gmtime())
        else:
            #print("troppo presto")
            return

        for n,t in self.task.items():
            #print("eseguo {}".format(n))
            t.kick()

    def remove_task(self, param):
        if param in self.task:
            del self.task[param]
            print("{} removed from scheduler".format(param))
        else:
            print("{} not found in the scheduler".format(param))
