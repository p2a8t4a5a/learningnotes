#! /usr/bin/env python

import socket
def post(d,port=8080):
    s = socket.socket()
    host = socket.gethostname()
    # host='45.63.124.217'
    #print 'before connect',d
    s.connect((host, port))
    #print 'connect start',d
    s.send(b'hello,server %d\n\n'%d)
    s.recv(1024)
    #print 'connect end',d

if __name__=="__main__":
    post(0)


