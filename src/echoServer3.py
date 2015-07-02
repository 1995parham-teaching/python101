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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('', 1373))
sock.listen(5)

while True:
    client = sock.accept()
    client = client[0]
    while True:
        buff = client.recv(1024)
        if buff:
            client.send(buff)
        else:
            break
