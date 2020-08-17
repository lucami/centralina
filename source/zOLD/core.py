from zOLD.AirSensor.airsensor_factory import *
from zOLD.DataHandler.DataHandlerFactory import *
from zOLD.WiFiManager.WiFi_Manager import WiFiManager
from zOLD.fileManager.FileManager import *
from zOLD.sensor2.gps_factory import *
import time
'''
pid = os.fork()
if pid is 0:
    #subprocess.call(['/home/debian/centralina/source/Bosh/bsp', '&'], shell=False)
    subprocess.popen(['/home/debian/centralina/source/Bosh/bsp', '&'], shell=False)
'''

'''
pid = os.fork()
if pid is 0:
    gpio_46 = GPIO46Manager()
    gpio_46.run()
'''

wifi_manager = WiFiManager()
file_manager = FileManager()

g_factory = gps_factory("nmea serial")
gps_facade = g_factory.get_facade()

aq_factory = airsensor_factory()
aq_facade = aq_factory.get_facade()

#bosh_factory = BoshFactory()
#bosh_facade = bosh_factory.get_facade()

dh_factory = DataHandler_Factory()
data_handler = dh_factory.get_data_handler()

s = Scheduler("task scheduler")

data_handler.add_sensor("Air Sensor Facade", aq_facade)
data_handler.add_sensor("gps Facade", gps_facade)
#data_handler.add_sensor("Bosh Facade", bosh_facade)

s.add_task(g_factory.get_parser(), "gps parser")
s.add_task(aq_factory.get_parser(), "air quality parser")
#s.add_task(bosh_factory.get_parser(), "bosh parser")
s.add_task(data_handler, "Data Handler")
s.add_task(wifi_manager, "WiFi Manager")

data_handler.register(file_manager, file_manager.data_update)

#launch_backend()

i = 0
while True:
    s.run()
    time.sleep(1)
# https://www.tanzolab.it/systemd
# https://www.mauras.ch/systemd-run-it-last.html
# sudo systemctl stop centralina
# /etc/systemd/system/centralina. service
# http://beaglebone.cameon.net/home/reading-the-analog-inputs-adc
# https://pythonforundergradengineers.com/index6.html
# https://www.fullstackpython.com/table-of-contents.html
'''
[Unit]
Description=Lancia core.py
After=serial-getty@ttyS4.service

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/debian/centralina/source/core.py
Restart=always
User=debian

[Install]
WantedBy=multi-user.target
'''
# https://pypi.org/project/PyAccessPoint/
# https://pypi.org/project/netifaces/
# https://pypi.org/project/wifi/
# https://gist.github.com/taylor224/516de7dd0b707bc0b1b3
# sudo vim /etc/default/hostapd
