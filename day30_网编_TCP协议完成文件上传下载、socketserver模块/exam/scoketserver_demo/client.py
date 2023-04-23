# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client.py
# @datatime: 2023/4/23 07:55

"""
目标：socketserver服务端的客户端程序
"""
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8081))

while True:
    sk.send(b'hello')
    content = sk.recv(1024).decode('utf-8')
    print(content)