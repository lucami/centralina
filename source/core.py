import sys
import os
from scheduler import *
import calendar
import time


sys.path.insert(0,'./sensor2')
from gps_factory import *

sys.path.insert(0,'./AirSensor')
from airsensor_factory import *


g_factory=gps_factory("nmea serial")
gps_facade = g_factory.get_facade()
'''print("GPS")
object_methods = [method_name for method_name in dir(gps_facade)
                  if callable(getattr(gps_facade, method_name))]
print (object_methods)
'''

aq_factory=airsensor_factory()
aq_facade = aq_factory.get_facade()


s = Scheduler("task scheduler")
s.add_task(g_factory.get_parser(), "gps parser")
s.add_task(aq_factory.get_parser(), "air quality parser")




i=0
while True:
    s.run()

    if gps_facade.data_ready() == True and aq_facade.data_ready()==True:
    #if aq_facade.new_airsensor_data()==1:
    #if gps_facade.data_ready() == True:

        os.system('clear')
        print("{}".format("GPS DATA: {}".format(gps_facade.get_data())))
        '''
        if i%2==0:
            print("*", end="")
        elif i%2==1:
            print(" ", end="")
        i+=1
        '''
        print("{}".format("AIR SENS: {}".format(aq_facade.get_data())))
