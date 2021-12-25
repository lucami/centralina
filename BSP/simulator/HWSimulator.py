import socket
from time import sleep
import random

localIP = "127.0.0.1"
bufferSize = 1024

DIG_IN_PORT = 1028
GPS_PORT = 1026
HTP_PORT = 1025
PM_PORT = 1027


def manage_dig_in(s):
    try:
        data, addr = s.recvfrom(1024)
        # print(f"Received: {data}")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print(message)
        return

    try:
        if len(data) > 0:
            if (random.randint(0, 1)) == 1:
                s.sendto(str.encode("1\x00"), addr)
            else:
                s.sendto(str.encode("0\x00"), addr)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print(message)


def manage_gps(s):
    try:
        data, addr = s.recvfrom(1024)
        # print(f"Received: {data}")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print(message)
        return

    try:
        if len(data) > 0:
            s.sendto(str.encode(
                "$GPRMC,173500.00,A,4137.39254,N,01320.01658,E,0.718,,251221,,,A*7B\n,A*6E\n$GPGGA,173500.00,4137.39254,N,01320.01658,E,1,05,1.49,184.7,M,42.5,M,,*5E\n$GPVTG,,T,,M,0.718,N,1.330,K,A*2C\n,A*38\n$GPGSA,A,3,32,29,24,12,02,,,,,,,,3.54,1.49,3.22*02\n5\n"),
                     addr)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print(message)


def manage_htp(s):
    try:
        data, addr = s.recvfrom(1024)
        # print(f"Received: {data}")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print(message)
        return

    try:
        if len(data) > 0:
            if (random.randint(0, 1)) == 1:
                s.sendto(str.encode("24.17;51.791992;992.26"), addr)
            else:
                s.sendto(str.encode("28.37;84.971680;992.2"), addr)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print(message)


def manage_pm(s):
    try:
        data, addr = s.recvfrom(1024)
        # print(f"Received: {data}")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print(message)
        return

    try:
        if len(data) > 0:
            if (random.randint(0, 1)) == 1:
                s.sendto(str.encode("10;11"), addr)
            else:
                s.sendto(str.encode("1000;1100"), addr)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # print(message)


def init_sim_environment():
    dig_in_srv_l = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    dig_in_srv_l.setblocking(False)
    dig_in_srv_l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    dig_in_srv_l.bind((localIP, DIG_IN_PORT))

    gps_srv_l = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    gps_srv_l.setblocking(False)
    gps_srv_l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    gps_srv_l.bind((localIP, GPS_PORT))

    htp_srv_l = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    htp_srv_l.setblocking(False)
    htp_srv_l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    htp_srv_l.bind((localIP, HTP_PORT))

    pm_srv_l = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    pm_srv_l.setblocking(False)
    pm_srv_l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    pm_srv_l.bind((localIP, PM_PORT))

    return dig_in_srv_l, gps_srv_l, htp_srv_l, pm_srv_l


def start_simulator():
    dig_in_srv, gps_srv, htp_srv, pm_srv = init_sim_environment()
    while True:
        manage_dig_in(dig_in_srv)
        manage_gps(gps_srv)
        manage_htp(htp_srv)
        manage_pm(pm_srv)

        sleep(1)


if __name__ == "__main__":
    start_simulator()
