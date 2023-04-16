# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_udp_demo1.py
# @datatime: 2023/4/16 19:01

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

server = ('192.168.0.103', 8082)
sk.sendto(b'nihao', server)
msg = sk.recv(1024)
print(msg)

