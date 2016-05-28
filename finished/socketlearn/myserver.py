#! /usr/bin/env python
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
import time
#10^4 time:13s

class Server(ThreadingMixIn, TCPServer): pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        # print 'Got connection',addr
        # time.sleep(2)
        self.wfile.write('thank you for connecting')


server = Server(('', 1111), Handler)
print 'start:'
server.serve_forever()
