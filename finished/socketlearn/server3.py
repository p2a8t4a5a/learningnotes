#! /usr/bin/python
import socket,select
#edge trigger
#10^5 time=75.2s


import time
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'


serversocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind(('0.0.0.0',8080))
serversocket.listen(1)
serversocket.setblocking(0)

epoll=select.epoll()
epoll.register(serversocket.fileno(),select.EPOLLIN| select.EPOLLET)

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
                try:
                    while True:
                        connection,address=serversocket.accept()
                        connection.setblocking(0)
                        epoll.register(connection.fileno(),select.EPOLLIN| select.EPOLLET)
                        connections[connection.fileno()]=connection
                        requests[connection.fileno()]=b""
                        responses[connection.fileno()]=response
                except socket.error:
                    pass
            elif event & select.EPOLLIN:
                try:
                    while True:
                      requests[fileno]+=connections[fileno].recv(1024)
                except socket.error:
                    pass
                #print 'reveived:',requests[fileno]
                if EOL1 in requests[fileno]:
                    epoll.modify(fileno,select.EPOLLOUT| select.EPOLLET)
            elif event & select.EPOLLOUT:
                try:
                    while responses[fileno]:
                        byteswriten=connections[fileno].send(responses[fileno])
                        responses[fileno]= responses[fileno][byteswriten:]
                except socket.error:
                    pass
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

