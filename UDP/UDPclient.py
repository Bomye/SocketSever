#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'YQ'


import socket
import struct
import sys


def Client():
    BUF_SIZE = 1204
    server_addr = ('127.0.0.1',8888)

    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    except socket.error,e:
        print "Creating Socket Failure.Error code:" + str(e[0]) + " Message: " + e[1]
        sys.exit()

    while True:
        data = raw_input("Please input data > ")
        client.sendto(data,server_addr) # 向服务器发送数据
        data,addr = client.recvfrom(BUF_SIZE) #从服务器接收数据
        print "Data: ",data
    client.close()


if __name__ == '__main__':
    client = Client()


