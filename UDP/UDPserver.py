#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'YQ'


import socket
import sys


#UDP服务器端
def Server():
    BUF_SIZE = 1024 # 设置缓冲区大小
    server_addr = ('127.0.0.1',8888) #IP和端口构成表示地址
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #生成新的套接字对象
    except socket.error,e:
        print "Creating Socket Failure.Error code:" + str(e[0]) + " Massage:" + e[1]
        sys.exit()
    print "Created Socket!"

    server.bind(server_addr) # 套接字绑定端口
    while True:
        print "Waiting for data"
        data, client_addr = server.recvfrom(BUF_SIZE)  #从客户端接收数据
        print 'Connected by', client_addr, ' Receive Data : ', data
        server.sendto(data,client_addr) # 发送数据给客户端
    server.close()


if __name__ == '__main__':
    server = Server()