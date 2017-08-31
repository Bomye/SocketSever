#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'YQ'


#python使用socket实现TCP支持HTTP协议的静态网页服务器
from multiprocessing import Process
import socket
import re


HTML_ROOT_DIR = './html'


class HTTPServer(object):
    '''服务器'''
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 生成一个新的socket对象
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #设置地址复用
        # self.server_socket.bind("", port)

    def start(self):
        '''开启服务器'''
        self.server_socket.listen(128)# 设置最大监听数量为128
        while True:
            client_socket,client_addr = self.server_socket.accept()# 接收TCP连接，并返回新的套接字和地址
            print (u"[%s,%s]用户连接成功..."%client_addr)
            handle_client_process = Process(target=self.handle_client,args=(client_socket))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self,client_socket):
        '''处理客户端请求'''
        request_data = client_socket.recv(1024)# 从客户端接收数据
        print("request_data: ",request_data)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print line

        request_start_line = request_lines[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode('utf-8').group(1))

        if "/" == file_name:
            file_name = "/index.html"

        try:
            file = open(HTML_ROOT_DIR + file_name,'rb')
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Fount\r\n"
            response_head_line = "server: My server\r\n"
            response_body = "The File is not Found!"
        else:
            file_data = file.read()
            file.close()

            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_head_line = "Server: My server\r\n"
            response_body = file_data.decode("utf-8")
        finally:
            response = response_start_line + response_head_line +'\r\n'+response_body
            print("response data: ",response)

            client_socket.send(bytes(response,"utf-8"))
            client_socket.close()

    def bind(self,port):
        self.server_socket.bind('',port)


def main():
    http_server = HTTPServer()
    http_server.bind(8888)
    http_server.start()


if __name__ == '__main__':
    main()

