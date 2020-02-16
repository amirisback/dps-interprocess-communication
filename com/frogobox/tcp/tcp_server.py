# import library socket karena akan menggunakan IPC socket
import socket
from com.frogobox.base.config import *

# definisikan alamat IP binding  yang akan digunakan
TCP_SERVER_IP = BASE_CONFIG_IP_ADDRESS

# definisikan port number binding  yang akan digunakan
TCP_SERVER_PORT = BASE_CONFIG_PORT

# definisikan ukuran buffer untuk mengirimkan pesan
TCP_SERVER_BUFFER = BASE_CONFIG_BUFFER

print(BASE_MESSAGE_CONNECTING)

# buat socket bertipe TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpServer:
    # lakukan bind
    tcpServer.bind((TCP_SERVER_IP, TCP_SERVER_PORT))

    # server akan listen menunggu hingga ada koneksi dari client
    tcpServer.listen()

    # menerima koneksi
    connection, address = tcpServer.accept()

    with connection:

        # lakukan loop forever
        while True:

            # menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
            print('Connected by \t: ', address)

            # menerima data berdasarkan ukuran buffer
            messageFromClient = connection.recv(TCP_SERVER_BUFFER)

            if not messageFromClient:
                break

            # menampilkan pesan yang diterima oleh server menggunakan print,
            print('Data \t\t\t:', str(messageFromClient, 'utf-8'))

            # mengirim kembali data yang diterima dari client kepada client
            connection.send(messageFromClient)

# tutup koneksi
tcpServer.close()
