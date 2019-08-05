from LowLevelInterface import *
from Poll_Thread import *
import queue

q1 = queue.Queue()
q2 = queue.Queue()

poll = SerialNMEASim(q1,1, "Poll Thread")
low = NMEA_Interface(q1, q2, 2, "Low Level interface Thread")

low.start()
poll.start()


while True:
    print(q2.get())
    q2.task_done()
