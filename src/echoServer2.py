# In The Name Of God
# ========================================
# [] File Name : echoServer2
#
# [] Creation Date : 15-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import asyncio


@asyncio.coroutine
def handle_echo(reader, writer):
    data = yield from reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    print("Send: %r" % message)
    writer.write(data)
    yield from writer.drain()

    print("Close the client socket")
    writer.close()


loop = asyncio.get_event_loop()
coroutine = asyncio.start_server(handle_echo, '127.0.0.1', 1373, loop=loop)
server = loop.run_until_complete(coroutine)

# Serve requests until CTRL+c is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

