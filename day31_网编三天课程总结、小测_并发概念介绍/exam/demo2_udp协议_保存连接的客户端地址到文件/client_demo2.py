# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_demo2.py
# @datatime: 2023/4/24 下午2:39

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

sk.sendto(b'hello', ('127.0.0.1', 9000))
msg = sk.recv(1024)
print(msg)
