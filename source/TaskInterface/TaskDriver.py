import os

from TaskInterface.QueueDefinition import TaskQueue
from TaskInterface.WiFi_Task_Commands import *


class test_task:
    def __init__(self):
        pid = os.fork()

        if pid is not 0:
            return

        q = TaskQueue("Test")

        if_on = Wlan0on()
        dhcp_on = DnsmasqOn()
        set_ip = SetIP()
        ap_on = HostapdOn()

        q.add_task(if_on)
        q.add_task(set_ip)
        q.add_task(dhcp_on)
        q.add_task(ap_on)

        q.run_next()
        q.run_next()
        q.run_next()
        q.run_next()


if __name__ == '__main__':
    t1 = Task("ls")
    t2 = Task("ls -la")
    q = TaskQueue("Test")

    if_on = Wlan0on()
    dhcp_on = DnsmasqOn()
    ap_on = HostapdOn()

    q.add_task(if_on)
    q.add_task(dhcp_on)
    q.add_task(ap_on)

    q.run_next()
    q.run_next()
    q.run_next()
