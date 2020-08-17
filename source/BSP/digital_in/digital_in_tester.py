import socket
import os
import time


pid=os.fork()

if pid == 0:
    time.sleep(2)

t=time.time()
UDP_IP = "127.0.0.1"
UDP_PORT = 1028
MESSAGE = b"a"

#print("UDP target IP: %s" % UDP_IP)
#print("UDP target port: %s" % UDP_PORT)
#print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
t1=time.time()
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data=sock.recvfrom(1024)
t2=time.time()
print(data)
