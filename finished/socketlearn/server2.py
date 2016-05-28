#! /usr/bin/python
#level trigger
#time=87.04s

import socket,select
import time
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'


serversocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind(('0.0.0.0',8080))
serversocket.listen(10000)
serversocket.setblocking(0)
#设置不要通话操作系统缓存立刻发送，适用即时应用
#serversocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
epoll=select.epoll()
epoll.register(serversocket.fileno(),select.EPOLLIN)

Max=0
Sum=0
try:
    connections={};requests={};responses={}
    while True:
        events=epoll.poll(1)

        t=len(events)
        Max=max(Max,t)
        Sum+=t
        print t,Max,Sum

        for fileno,event in events:
            if fileno==serversocket.fileno():
                connection,address=serversocket.accept()
                connection.setblocking(0)
                epoll.register(connection.fileno(),select.EPOLLIN)
                connections[connection.fileno()]=connection
                requests[connection.fileno()]=b""
                responses[connection.fileno()]=response
            elif event & select.EPOLLIN:
                requests[fileno]+=connections[fileno].recv(1024)
                #print 'reveived:',requests[fileno]
                if EOL1 in requests[fileno]:
                    epoll.modify(fileno,select.EPOLLOUT)
                    #适用于http，憋着信息(不是很理解)
                    #connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
            elif event & select.EPOLLOUT:
                byteswriten=connections[fileno].send(responses[fileno])
                responses[fileno]= responses[fileno][byteswriten:]
                if not responses[fileno]:
                    epoll.modify(fileno,select.EPOLLHUP)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()

