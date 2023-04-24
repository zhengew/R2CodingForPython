# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server.py
# @datatime: 2023/4/24 下午2:22

"""
练习1:tcp协议实现客户端发来的消息转换成大写
"""

import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 8082))
sk.listen()

while True:
    conn,_ = sk.accept()
    while True:
        msg = conn.recv(1024).decode('utf-8')
        conn.send(msg.upper().encode('utf-8'))
        if msg.upper() == 'Q':
            break