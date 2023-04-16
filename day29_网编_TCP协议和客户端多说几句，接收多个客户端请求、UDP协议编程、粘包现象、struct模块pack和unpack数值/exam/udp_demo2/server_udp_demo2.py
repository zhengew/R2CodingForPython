# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_udp_demo2.py
# @datatime: 2023/4/16 19:07

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('192.168.0.103', 8083))

while True:
    msg, addr = sk.recvfrom(1024)
    if msg.decode('utf-8').upper() == 'Q':
        sk.sendto(msg, addr)
    print(msg.decode('utf-8'), addr)

    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'), addr)