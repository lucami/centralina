import socket


server_address = 'socket'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.bind(server_address)

while True:
    a=sock.recv(1024)
    print(a)