# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: online_char_client_v2.py
# @datatime: 2023/4/19 07:57

"""
客户端
"""
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('127.0.0.1', 8081)

