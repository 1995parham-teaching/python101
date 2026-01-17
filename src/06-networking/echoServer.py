"""
Topic: TCP Echo Server with select()
Concepts: socket programming, select for I/O multiplexing, non-blocking server
Learning objectives:
    - Create a TCP server using the socket module
    - Handle multiple clients with select() (I/O multiplexing)
    - Understand the select-based event loop pattern

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

import select
import socket

# Create TCP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# Bind to all interfaces on port 1373
server.bind(("", 1373))

# Listen for connections (backlog of 5)
server.listen(5)

# List of sockets to monitor for reading
read_list_check = [server]
client_list = []

print("Echo server running on port 1373...")
print("Connect with: nc localhost 1373")

while True:
    # select() blocks until at least one socket is ready
    # Returns lists of readable, writable, and error sockets
    read_list_ready, write_list_ready, exp_list_ready = select.select(
        read_list_check, [], []
    )

    # Check if server socket has a new connection
    if read_list_ready.count(server) > 0:
        # Accept the new connection
        client, client_address = server.accept()
        print(f"Connection from {client_address[0]}:{client_address[1]}")
        # Add client to monitoring lists
        read_list_check.append(client)
        client_list.append(client)

    # Process data from connected clients
    for client in client_list:
        if read_list_ready.count(client) > 0:
            # Receive up to 1024 bytes
            data = client.recv(1024)
            if not data:
                # Empty data means client disconnected
                print("Client disconnected")
                client.close()
                client_list.remove(client)
                read_list_check.remove(client)
                continue
            # Echo the data back
            print("Received:", data)
            client.send(data)


# === Expected Output ===
# Echo server running on port 1373...
# Connect with: nc localhost 1373
# Connection from 127.0.0.1:54321
# Received: b'Hello\n'
# (server echoes 'Hello' back to client)

# === Exercises ===
# 1. Add a broadcast feature that sends received messages to all clients
# 2. Add a simple command protocol (e.g., "quit" to disconnect)
