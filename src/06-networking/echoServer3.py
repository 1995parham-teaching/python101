"""
Topic: Threaded Echo Server
Concepts: threading, socket programming, concurrent connections
Learning objectives:
    - Handle multiple clients using threads
    - Create a thread per connection pattern
    - Understand threading vs asyncio approaches

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import socket
import threading


class Handler(threading.Thread):
    """
    Thread handler for a single client connection.

    Each client gets its own thread, allowing concurrent handling.
    """

    def __init__(self, client_socket):
        """
        Initialize the handler thread.

        Args:
            client_socket: The connected client's socket
        """
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        """
        Thread entry point - handles client communication.

        Runs in a loop, echoing data until client disconnects.
        """
        print(f"Handler thread started: {threading.current_thread().name}")
        while True:
            # Receive data from client
            buff = self.client_socket.recv(1024)
            if buff:
                # Echo data back
                print(f"Echoing: {buff}")
                self.client_socket.send(buff)
            else:
                # Empty data = client disconnected
                print("Client disconnected")
                break
        self.client_socket.close()


# Create and configure server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow port reuse
sock.bind(("", 1373))
sock.listen(5)

print("Threaded echo server running on port 1373...")
print("Connect with: nc localhost 1373")

while True:
    # Accept new connection (blocks until client connects)
    client = sock.accept()
    print(f"New connection from {client[1]}")

    # Spawn a new thread for this client
    Handler(client[0]).start()


# === Expected Output ===
# Threaded echo server running on port 1373...
# Connect with: nc localhost 1373
# New connection from ('127.0.0.1', 54321)
# Handler thread started: Thread-1
# Echoing: b'Hello\n'
# Client disconnected

# === Exercises ===
# 1. Add a thread pool to limit the number of concurrent connections
# 2. Add graceful shutdown handling with a shared flag
