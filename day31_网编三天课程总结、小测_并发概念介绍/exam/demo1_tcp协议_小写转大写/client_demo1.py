# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_demo1.py
# @datatime: 2023/4/24 下午2:23

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8082))

while True:
    msg = input('>>>').strip()
    sk.send(msg.encode('utf-8'))
    content = sk.recv(1024).decode('utf-8')
    if content == 'Q':
        break
    print(content)
