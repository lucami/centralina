from TaskInterface.QueueDefinition import TaskQueue
from TaskInterface.WiFi_Task_Commands import Wlan0on, DnsmasqOn, SetIP, HostapdOn, Wlan0off, DnsmasqOff, HostapdOff


class WLanOn(TaskQueue):
    def __init__(self):
        self.q = TaskQueue("Wlan ON")

        on = Wlan0on()
        dhcp = DnsmasqOn()
        ip = SetIP()
        ap = HostapdOn()

        self.q.add_task(on)
        self.q.add_task(dhcp)
        self.q.add_task(ip)
        self.q.add_task(ap)

    def run(self):
        self.q.run_next()
        self.q.run_next()
        self.q.run_next()
        self.q.run_next()
        self.q.wrap_index()


class WLanOff(TaskQueue):
    def __init__(self):
        self.q = TaskQueue("WLan Off")

        self.q.add_task(Wlan0off())
        self.q.add_task(DnsmasqOff())
        self.q.add_task(HostapdOff())

    def run(self):
        self.q.run_next()
        self.q.run_next()
        self.q.run_next()
        self.q.run_next()
        self.q.wrap_index()


'''
class WLanOn(Command):
    def __init__(self):
        self.command = ["connmanctl", "enable", "wifi"]
        self.f = open("/home/debian/onlog.txt", "a")

    def run(self):
        rval = False

        self.f.write("Try to enable wifi...")
        print("Try to enable wifi...")
        p = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()
        print(output)
        print(errors)
        if len(output) == 0 and "Already enabled" in errors:
            rval = True
        elif len(errors) == 0 and "Enabled wifi" in output:
            rval = True

        self.f.write(output)
        self.f.write(errors)

        p = subprocess.Popen("ifconfig", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()
        self.f.write(output)
        self.f.write(errors)
        self.f.flush()
        return rval


class WLanOff(Command):
    def __init__(self):
        self.command = ["connmanctl", "disable", "wifi"]
        self.f = open("/home/debian/offlog.txt", "a")

    def run(self):
        rval = False

        p = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()
        print(output)
        print(errors)
        if len(output) == 0 and "Already disabled" in errors:
            rval = True
        elif len(errors) == 0 and "Disabled wifi" in output:
            rval = True

        self.f.write(output)
        self.f.write(errors)

        p = subprocess.Popen("ifconfig", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()
        self.f.write(output)
        self.f.write(errors)
        self.f.flush()
        return rval


if __name__ == '__main__':
    off = WLanOff()
    print(off.run())
    print(off.run())
    on = WLanOn()
    print(on.run())
    print(on.run())
'''
