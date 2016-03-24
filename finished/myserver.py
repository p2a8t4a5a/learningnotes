#! /usr/bin/env python
from SocketServer import TCPServer ,ThreadingMixIn,StreamRequestHandler

class Server(ThreadingMixIn,TCPServer):pass

class Handler(StreamRequestHandler):
	def handle(self):
		addr=self.request.getpeername()
		print 'Got connection',addr
		self.wfile.write('thank you for connecting')

server=Server(('',1234),Handler)
print 'start:'
server.serve_forever()

