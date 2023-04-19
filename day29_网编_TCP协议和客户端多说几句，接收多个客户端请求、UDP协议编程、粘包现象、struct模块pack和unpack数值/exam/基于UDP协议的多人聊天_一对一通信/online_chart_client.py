# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: online_chart_client.py
# @datatime: 2023/4/18 20:11

"""
多人聊天客户端
"""

import socket

name=input('请输入您的名字>>>').strip()
sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('192.168.0.103',9001)
while True:
    send_msg = input('请输入您的留言>>>')
    if send_msg.upper() == 'Q': break
    send_msg = name+': '+send_msg
    sk.sendto(send_msg.encode('utf-8'),server)
    recv_msg = sk.recv(1024).decode('utf-8')
    if recv_msg.upper() == 'Q': break
    print(recv_msg)

