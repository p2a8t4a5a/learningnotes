#! /usr/bin/python
import socket
import time
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'


serversocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind(('0.0.0.0',8080))
serversocket.listen(1)

try:
    while True:
        connectionclient,address=serversocket.accept()
        requset=b''
        requset+=connectionclient.recv(1024)
        print (requset.decode())
        connectionclient.send(response)
        time.sleep(2)
        connectionclient.close()
finally:
    serversocket.close()
