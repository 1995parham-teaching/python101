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
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind(('', 1373))
server.listen(5)

read_list_check = [server]
client_list = []

while True:
    read_list_ready, write_list_ready, exp_list_ready = select.select(read_list_check, [], [])

    if read_list_ready.count(server) > 0:
        # Accept connection with server socket.
        client, client_address = server.accept()
        print("Connection from %s:%d" % (client_address[0], client_address[1]))
        read_list_check.append(client)
        client_list.append(client)

    for client in client_list:
        if read_list_ready.count(client) > 0:
            data = client.recv(1024)
            if not data:
                client.close()
                continue
            print("data =", data)
            client.send(data)