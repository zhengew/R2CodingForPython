# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_udp_demo2.py
# @datatime: 2023/4/16 19:08

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('192.168.0.103', 8083)

while True:
    send_msg = input('>>>')
    if send_msg == 'Q': break # 客户端单方面断开
    sk.sendto(send_msg.encode('utf-8'), server)
    msg = sk.recv(1024).decode('utf-8')
    print(msg, server)
    if msg.upper() == 'Q':
        break

sk.close()