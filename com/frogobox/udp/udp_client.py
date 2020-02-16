#! /usr/bin/python3

# import library socket karena akan menggunakan IPC socket
import socket
from com.frogobox.base.config import *

# definisikan target IP server yang akan dituju
UDP_IP = BASE_CONFIG_IP_ADDR

# definisikan target port number server yang akan dituju
UDP_PORT = BASE_CONFIG_PORT
TARGET = (UDP_IP, UDP_PORT)
MESSAGE = 'UDP ' + MESSAGE_REQUEST

# buat socket bertipe UDP
with socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
) as udpClient:
    udpClient.connect(TARGET)
    for x in range(10):
        udpClient.sendto(str(MESSAGE + ' pesan ke - ' + str(x + 1)).encode(), TARGET)
udpClient.close()
