"""
Topic: Async Echo Server with asyncio (Legacy Syntax)
Concepts: asyncio, coroutines with @asyncio.coroutine, yield from, event loop
Learning objectives:
    - Understand the legacy asyncio coroutine syntax
    - Use asyncio.start_server for async networking
    - Learn about the event loop pattern

Note: This uses the older @asyncio.coroutine/yield from syntax.
      Modern Python (3.5+) prefers async/await - see echoServer3.py variant.

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import asyncio


@asyncio.coroutine  # type: ignore[attr-defined]
def handle_echo(reader, writer):
    """
    Handle a single client connection.

    This coroutine is called for each new connection.
    Uses legacy 'yield from' syntax (modern: 'await').
    """
    # Read data from client (yield from = await in modern syntax)
    data = yield from reader.read(1024)
    message = data.decode()

    # Get client address info
    addr = writer.get_extra_info("peername")
    print(f"Received {message!r} from {addr!r}")

    # Echo the data back
    print(f"Send: {message!r}")
    writer.write(data)
    yield from writer.drain()  # Ensure data is sent

    # Close the connection
    print("Close the client socket")
    writer.close()


# Get the event loop
loop = asyncio.get_event_loop()

# Create the server coroutine
coroutine = asyncio.start_server(handle_echo, "127.0.0.1", 1373, loop=loop)

# Run until server is created
server = loop.run_until_complete(coroutine)

# Serve requests until Ctrl+C
print(f"Serving on {server.sockets[0].getsockname()}")
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Cleanup
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()


# === Expected Output ===
# Serving on ('127.0.0.1', 1373)
# Received 'Hello\n' from ('127.0.0.1', 54321)
# Send: 'Hello\n'
# Close the client socket

# === Exercises ===
# 1. Convert this to use async/await syntax (Python 3.5+)
# 2. Keep the connection open for multiple messages (remove the close)
