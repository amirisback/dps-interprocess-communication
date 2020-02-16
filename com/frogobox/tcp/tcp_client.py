# import library socket karena akan menggunakan IPC socket
import socket
from com.frogobox.base.config import *

# definisikan tujuan IP server
TCP_SERVER_IP = BASE_CONFIG_IP_ADDRESS

# definisikan port dari server yang akan terhubung
TCP_SERVICE_PORT = BASE_CONFIG_PORT

# definisikan ukuran buffer untuk mengirimkan pesan
TCP_SERVER_BUFFER = BASE_CONFIG_BUFFER

# definisikan pesan yang akan disampaikan
TCP_MESSAGE = 'TCP ' + MESSAGE_REQUEST

# buat socket TCP
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
tcpClient.connect((TCP_SERVER_IP, TCP_SERVICE_PORT))

# kirim pesan ke server, pesan bebas, dan ditambahkan nama anggota kelompok
tcpClient.send(TCP_MESSAGE.encode())

# terima pesan dari server
messageFromServer = tcpClient.recv(TCP_SERVER_BUFFER)

# tampilkan pesan/reply dari server
print('Received', messageFromServer.decode())

# tutup koneksi
tcpClient.close()
