import socket

# Create a socket object
s = socket.socket()
# Get local machine name
host = socket.gethostname()
# Reserve a port for your service.
port = 1378
# Bind to the port
s.bind((host, port))

# Now wait for client connection.
s.listen(5)
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print(f"Got connection from {addr}")
    c.send("Thank you for connecting".encode("utf-8"))
    # Close the connection
    c.close()
