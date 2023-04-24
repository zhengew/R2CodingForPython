# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_demo2.py
# @datatime: 2023/4/24 下午2:38

"""
练习2：udp协议将所有发送新的客户端ip和端口都写到文件
"""

import socket
import json

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))

while True:
    msg, addr = sk.recvfrom(1024)
    sk.sendto(msg, addr)
    with open('client_addr', mode='at', encoding='utf-8') as f:
        client_info = {'ip': addr[0], 'port': addr[1]}
        f.write(json.dumps(client_info) + '\n')
    print(addr)
