#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'YQ'

import socket
import sys

#客户端
def Client():
    BUF_SIZE = 1024
    server_addr = ('127.0.0.1',8888)
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 返回新的socket对象
    except socket.error,e:
        print "Creating Socket Failure. Error Code : " + str(e[0]) + " Message : " + e[1]
        sys.exit()
    try:
        client.connect(server_addr) # 要连接的服务器地址
    except socket.error,e:
        print u'连接错误：',e
        sys.exit()
    print u"连接成功！"

    while  True:
        data = raw_input("Please input some string >")
        if not data:
            print "Input can't empty,Please input again..."
            continue
        client.sendall(data) # 发送数据到服务器
        data = client.recv(BUF_SIZE) # 从服务器接收数据
        print data
    client.close()


if __name__ == '__main__':
    client = Client()