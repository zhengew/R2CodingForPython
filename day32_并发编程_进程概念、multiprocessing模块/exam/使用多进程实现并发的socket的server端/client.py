# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client.py
# @datatime: 2023/4/27 下午5:17

"""
并发的socket的client端
"""

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

while True:
    sk.send(b'hello')
    msg = sk.recv(1024)
    print(msg)