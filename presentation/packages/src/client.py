# import socket module
import socket

# create a socket object
s = socket.socket()
# get local machine name
host = socket.gethostname()
# set port equals to the service port
port = 1378

# create connection to the service.
s.connect((host, port))

print(s.recv(1024).decode("utf-8"))
# close the socket when done
s.close()
