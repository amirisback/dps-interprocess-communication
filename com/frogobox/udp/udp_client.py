# import library socket karena akan menggunakan IPC socket
import socket
from com.frogobox.base.config import *

# definisikan target IP server yang akan dituju
UDP_SERVER_IP = BASE_CONFIG_IP_ADDRESS

# definisikan target port number server yang akan dituju
UDP_SERVER_PORT = BASE_CONFIG_PORT
UDP_MESSAGE = 'UDP ' + MESSAGE_REQUEST

print('Sending Message ' + UDP_MESSAGE)

# buat socket bertipe UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udpClient:
    udpClient.connect((UDP_SERVER_IP, UDP_SERVER_PORT))
    for x in range(10):
        udpClient.sendto(str(UDP_MESSAGE + ' pesan ke - ' + str(x + 1)).encode(), (UDP_SERVER_IP, UDP_SERVER_PORT))
udpClient.close()
