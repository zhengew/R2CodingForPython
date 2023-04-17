# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_udp_demo1.py
# @datatime: 2023/4/16 19:01

"""
目标: UDP协议，一对一通信
"""
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)      # 创建udp协议的sk对象
sk.bind(('192.168.0.103', 8081))                # 申请系统资源 ip、端口
while True:
    msg, addr = sk.recvfrom(1024)               # 接收客户端请求，返回值为接收的消息和地址
    print(msg, addr)
    print(msg.decode('utf-8'))
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'), addr)   # 发送消息




