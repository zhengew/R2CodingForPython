# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_udp_demo1.py
# @datatime: 2023/4/16 19:01
"""
目标: UDP协议客户端
实现客户端主动退出或服务端请求退出
"""
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)          # 创建客户端udp协议的sk对象
server = ('192.168.0.103', 8081)                    # 服务端地址

while True:                                         # 客户端与服务端通信
    send_msg = input('>>>').strip()
    if send_msg.upper() == 'Q':
        break
    sk.sendto(send_msg.encode('utf-8'), server)     # 客户端与服务端创建链接
    recv_msg = sk.recv(1024).decode('utf-8')        # 接收服务端消息
    if recv_msg.upper() == 'Q':
        break
    print(recv_msg)

sk.close()

