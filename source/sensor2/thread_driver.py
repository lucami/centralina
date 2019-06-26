from LowLevelInterface import *
from Poll_Thread import *
from parser import *
import queue
sys.path.insert(0,'./sensor')
from scheduler import *
from kick import *

q1 = queue.Queue()
q2 = queue.Queue()

poll = SerialNMEASim(q1,1, "Poll Thread")
low = NMEA_Interface(q1, q2, 2, "Low Level interface Thread")
parser = NMEA_Parser(q2)

low.start()
poll.start()

s = Scheduler("task scheduler")
s.add_task(parser, "parser")

while True:
    s.run()
