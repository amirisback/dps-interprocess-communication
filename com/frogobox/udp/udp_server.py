# import library socket karena akan menggunakan IPC socket
import socket
from com.frogobox.base.config import *

# Berikan tampilan (print bahwa socket berhasil dibuat)
# print('Socket berhasil dibuat', socket)

# definisikan alamat IP bind dari server
IP_ADDR = BASE_CONFIG_IP_ADDR

# definisikan port number untuk bind dari server
PORT = BASE_CONFIG_PORT
BUFFER = BASE_CONFIG_BUFFER
ADDR = (IP_ADDR, PORT)

# buat socket bertipe UDP
with socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
) as udpServer:
    # lakukan bind
    udpServer.bind(ADDR)

    # Berikan tampilan (print) bahwa socket bind ke alamat IP dengan port yang telah didapatkan
    # print(udpServer)

    # loop forever
    while True:
        # terima pesan dari client
        data, address = udpServer.recvfrom(BUFFER)

        if not data:
            break

        # menampilkan hasil pesan dari client
        print('Data \t\t\t:', data.decode())

        # print (addr)
        print('Received from \t: ', address)
        print()

udpServer.close()