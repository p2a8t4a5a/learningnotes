# !/usr/bin/python
# -*- encoding:utf-8 -*-
import os,sys

# rfc1035
# format
# +---------------------+
# |        Header       |
# +---------------------+
# |       Question      | the question for the name server
# +---------------------+
# |        Answer       | RRs answering the question
# +---------------------+
# |      Authority      | RRs pointing toward an authority
# +---------------------+
# |      Additional     | RRs holding additional information
# +---------------------+
#
# header
#                                 1  1  1  1  1  1
#   0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
# |                      ID                       |
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
# |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
# |                    QDCOUNT                    |
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
# |                    ANCOUNT                    |
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
# |                    NSCOUNT                    |
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
# |                    ARCOUNT                    |
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
import socket
import struct


def build_address(address):
    address = address.strip(b'.')
    labels = address.split('.')
    results = []
    for label in labels:
        l = len(label)
        if l > 63:
            return None
        results.append(chr(l))
        results.append(label)
    results.append(b'\0')
    return b''.join(results)


QTYPE_A = 1  # host address
QCLASS_IN = 1  # the Internet


def build_request(hostname, qtype):
    id = os.urandom(2)
    header = struct.pack("!BBHHHH", 1, 0, 1, 0, 0, 0)
    addr = build_address(hostname)
    qtype_class = struct.pack('!HH', qtype, QCLASS_IN)
    return id + header + addr + qtype_class


def check_head(response):
    RECODE = struct.unpack('!B', response[3])[0]
    if RECODE & 15:
        print 'error:', RECODE & 15
        return False
    return True


# return IP_address
def read_response(response):
    # check head
    if not check_head(response[:12]):
        return None

    # 回答数
    ANCOUNT = struct.unpack('!H', response[6:8])
    print 'ANCOUNT: ', ANCOUNT

    # get question
    t = 12
    while 1:
        num = struct.unpack('!B', response[t])[0]
        t += 1
        if num == 0:
            break
        question = struct.unpack('!' + str(num) + 's', response[t:t + num])
        t += num
        print question
    # read_status
    t+=4
    # get response name
    num = struct.unpack('!B', response[t])[0]
    if num & int('11000000',2):
        pass
    else:
        raise Exception('error 97')
    t+=2
    RES_CLASS=struct.unpack('!H',response[t:t+2])[0]
    if RES_CLASS==1:
        t+=8
        LENGTH=struct.unpack('!H',response[t:t+2])[0]
        if LENGTH==4:
            t+=2
            return struct.unpack('!BBBB',response[t:t+4])
        else:
            print 110,LENGTH
    else:
        print 112,RES_CLASS
    return None

def resolve(hostname, qtype):
    req = build_request(hostname, qtype)
    req_socket = socket.socket(socket.AF_INET,
                               socket.SOCK_DGRAM,
                               socket.SOL_UDP)
    req_socket.sendto(req, ('8.8.4.4', 53))
    response = req_socket.recv(1024)
    ip = read_response(response)
    return hostname, ip


if __name__ == "__main__":
    print resolve('wantjr.com', QTYPE_A)
