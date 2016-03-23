#! /usr/bin/env python

import socket
s=socket.socket()

host=socket.gethostname()
#host='45.63.124.217'

port=1234

s.connect((host,port))
print s.recv(1024)
