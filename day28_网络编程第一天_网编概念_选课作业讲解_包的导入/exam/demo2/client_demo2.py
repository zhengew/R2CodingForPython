# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_demo2.py
# @datatime: 2023/4/15 21:45

import socket

while True:
    sk = socket.socket()
    sk.connect(('127.0.0.1', 8080))

    sk.send(b'nihao')
    msg = sk.recv(1024)
    print(msg)

sk.close()