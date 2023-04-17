# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_demo1.py
# @datatime: 2023/4/16 17:49

"""
目标：TCP协议实现客户端和服务端多说几句化
"""
import socket

sk = socket.socket()
sk.connect(('192.168.0.103', 9094)) # 三次握手
print(sk)

while True:
    send_msg = input('>>>')
    sk.send(send_msg.encode('utf-8'))
    if send_msg.upper() == 'Q':
        break
    recv_msg = sk.recv(1024).decode('utf-8')
    if recv_msg.upper() == 'Q':
        break
    print(recv_msg)

sk.close() # 四次挥手