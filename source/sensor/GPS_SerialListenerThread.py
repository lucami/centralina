import threading
import time


class SerialListener(threading.Thread):

    def run(self):

        dev="/dev/ttyS4"
        f = open(dev,"r")
        s.app
        while True:
            s=f.readline()

        print("{} started!".format(self.getName()))              # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"



def main():
    for x in range(4):                                     # Four times...
        mythread = SerialListener(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, invoke the run method
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another


main()
