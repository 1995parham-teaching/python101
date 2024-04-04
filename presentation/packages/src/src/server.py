import socket

# create a socket object
s = socket.socket()
# get local machine name which means 127.0.0.1
# you can also use:
# host = '127.0.0.1'
# or
# host = '0.0.0.0'
host = socket.gethostname()
# reserve a port for your service.
port = 1378
# bind to the port
s.bind((host, port))

# now wait for client connection.
s.listen(5)
while True:
    # establish connection with client by accepting it.
    c, addr = s.accept()
    print(f"Got connection from {addr}")
    c.send("Thank you for connecting".encode("utf-8"))
    # close the connection
    c.close()
