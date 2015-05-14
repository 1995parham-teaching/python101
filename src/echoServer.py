# In The Name Of God
# ========================================
# [] File Name : echoServer.py
#
# [] Creation Date : 15-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind(('', 1373))
server.listen(5)
run = True

while run:
    client, client_address = server.accept()
    print("Connection from %s:%d" % (client_address[0], client_address[1]))
    while True:
        data = client.recv(1024)
        if not data:
            break
        print("data =", data)
        client.send(data)
    client.close()