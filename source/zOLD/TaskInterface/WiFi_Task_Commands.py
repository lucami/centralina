from zOLD.TaskInterface.TaskDefinition import Task

class SetIP(Task):
    def __init__(self):
        super().__init__("sudo ifconfig wlan0 10.0.0.1/24")

class Wlan0on(Task):
    def __init__(self):
        super().__init__("sudo ifconfig wlan0 up")


class Wlan0off(Task):
    def __init__(self):
        super().__init__("sudo ifconfig wlan0 down")


class DnsmasqOn(Task):
    def __init__(self):
        super().__init__("sudo systemctl start dnsmasq")


class DnsmasqOff(Task):
    def __init__(self):
        super().__init__("sudo systemctl stop dnsmasq")


class HostapdOn(Task):
    def __init__(self):
        super().__init__("sudo /usr/sbin/hostapd /home/debian/hostapd_test/hostapd.conf")


class HostapdOff(Task):
    def __init__(self):
        super().__init__("sudo /usr/bin/pkill hostapd")
