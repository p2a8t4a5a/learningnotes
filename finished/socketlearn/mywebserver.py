#! /usr/bin/python
import socket
import time

httpheader = '''''\
HTTP/1.1 200 OK
Context-Type: text/html
Server: Python-slp version 1.0
Context-Length: '''

def httpresponse(httpheader,htmlfile):
    content=""
    with open(htmlfile) as f:
        content=''.join(f.readlines())
    return "%s %d\n\n%s\n\n"%(httpheader,len(content),content)

def run(host,port):
    serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind((host,port))
    serversocket.listen(20)

    while True:
        clientsocket,addr=serversocket.accept()
        data=clientsocket.recv(1024)
        print 'reveived:\n'+data
        clientsocket.send(httpresponse(httpheader,'data.in'))
        time.sleep(1)
        clientsocket.close()

if __name__=='__main__':
    run('127.0.0.1',8888)






