import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 1378  # Reserve a port for your service.

s.connect((host, port))
print(s.recv(1024))
s.close()  # Close the socket when done
