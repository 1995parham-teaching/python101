# In The Name Of God
# ========================================
# [] File Name : echoServer3.py
#
# [] Creation Date : 02-07-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import socket
import threading


class Handler(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        while True:
            buff = self.client_socket.recv(1024)
            if buff:
                self.client_socket.send(buff)
            else:
                break


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('', 1373))
sock.listen(5)

while True:
    client = sock.accept()
    Handler(client[0]).start()
