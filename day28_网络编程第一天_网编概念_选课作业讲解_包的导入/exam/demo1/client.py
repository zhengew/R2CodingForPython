# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client.py
# @datatime: 2023/4/15 19:57

import socket

sk = socket.socket()
sk.connect(('172.16.238.5', 8081))

msg = sk.recv(1024)
print(msg)
sk.send(b'byebye')

sk.close()