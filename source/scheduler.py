from kick import *

class Scheduler:
    def __init__(self, name):
        self.name = name
        self.task = {}

    def add_task(self, kicker, name = None):
        if name == None:
            name = kicker
        print("{} put in the scheduler".format(name))
        self.task.update({name: kicker})

    def run(self):
        for n,t in self.task.items():
            #print("eseguo {}".format(n))
            t.kick()
    def remove_task(self, param):
        if param in self.task:
            del self.task[param]
            print("{} removed from scheduler".format(param))
        else:
            print("{} not found in the scheduler".format(param))

