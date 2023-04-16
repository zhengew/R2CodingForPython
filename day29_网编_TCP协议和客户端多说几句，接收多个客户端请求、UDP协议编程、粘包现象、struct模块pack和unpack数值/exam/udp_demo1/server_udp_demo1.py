# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_udp_demo1.py
# @datatime: 2023/4/16 19:01

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('192.168.0.103', 8082))

msg, addr = sk.recvfrom(1024)
print(msg)
sk.sendto(b'hello', addr)
