import os
import subprocess


class Task:
    def __init__(self, cmd, positive=None, negative=None):
        self.cmd = cmd.split()
        self.positive = positive
        self.negative = negative

    def run(self):
        #print("Task run: {}".format(self.cmd))

        p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        '''
        output, errors = p.communicate()

        print("Out: {}".format(output))
        print("Err: {}".format(errors))
        print("Ret: {}".format(p.returncode))

        return p.returncode
        '''