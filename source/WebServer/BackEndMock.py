import socket  # Import socket module
import threading


def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        # do some checks and if msg == someWeirdSignal: break:
        print(addr)
        print(msg)
        # msg = raw_input('SERVER >> ')
        # Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        # clientsocket.send(msg)
    clientsocket.close()


s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 6660  # Reserve a port for your service.

print('Server started!')
print('Waiting for clients...')

s.bind(("127.0.0.1", port))  # Bind to the port

while True:
    print("a")
    s.listen(5)  # Now wait for client connection.
    c, addr = s.accept()  # Establish connection with client.
    print('Got connection from', addr)
    t = threading.Thread(target=on_new_client, args=(c, addr))
    t.start()
    #threading.start_new_thread(on_new_client, (c, addr))

s.close()
