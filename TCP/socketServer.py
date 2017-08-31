#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'YQ'


import socket
import commands
import sys


#服务器端
def Server():
    BUF_SIZE = 1024
    server_addr = ('127.0.0.1',8888) #IP和端口构成表示地址
    try:
        # 生成一个新的socket对象
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET(IPV4网络协议) SOCK_STREAM(TCP协议)
    except socket.error,e:
        print "Creating Socket Failure.Error code:"+str(e[0]) + " Message:"+e[1]
        sys.exit()
    print "Socket Created!"

    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # 设置地址复用
    try:
        server.bind(server_addr) # 绑定地址
    except socket.error,e:
        print "Blinding Failure.Error code:" + str(e[0]) + " Massage:" + e[1]
        sys.exit()
    print "Socket Blind!"

    server.listen(5) # 设置最大监听数量为5
    while True:
        client,client_addr = server.accept() # 接收TCP连接，并返回新的套接字和地址
        print 'Connected by',client_addr
        while True:
            data = client.recv(BUF_SIZE) # 从客户端接收数据
            print data
            client.sendall(data) # 发送数据到客户端
    server.close()

if __name__ == '__main__':
    a = Server()
