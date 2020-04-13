import subprocess


class Command:
    def __init__(self):
        pass

    def run(self):
        pass


class WLanOn(Command):
    def __init__(self):
        self.command = ["connmanctl", "enable", "wifi"]
        self.f = open("/home/debian/onlog.txt", "a")

    def run(self):
        rval = False

        p = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()

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
