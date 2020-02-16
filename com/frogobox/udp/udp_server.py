# import library socket karena akan menggunakan IPC socket
import socket
from com.frogobox.base.config import *

# Berikan tampilan (print bahwa socket berhasil dibuat)
print("Socket Has Been Created")
print(BASE_MESSAGE_CONNECTING)
print()

# definisikan alamat IP bind dari server
UDP_SERVER_IP = BASE_CONFIG_IP_ADDRESS

# definisikan port number untuk bind dari server
UDP_SERVER_PORT = BASE_CONFIG_PORT
UDP_SERVER_BUFFER = BASE_CONFIG_BUFFER

# buat socket bertipe UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udpServer:
    # lakukan bind
    udpServer.bind((UDP_SERVER_IP, UDP_SERVER_PORT))

    # Berikan tampilan (print) bahwa socket bind ke alamat IP dengan port yang telah didapatkan

    # loop forever
    while True:
        # terima pesan dari client
        messageFromClient, address = udpServer.recvfrom(UDP_SERVER_BUFFER)

        if not messageFromClient:
            break

        # menampilkan hasil pesan dari client
        print('Data \t\t\t:', messageFromClient.decode())

        # print (addr)
        print('Received from \t: ', address)
        print()

udpServer.close()
