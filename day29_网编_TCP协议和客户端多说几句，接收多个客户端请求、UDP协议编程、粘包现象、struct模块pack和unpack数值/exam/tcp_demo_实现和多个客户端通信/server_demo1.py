
# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_demo1.py
# @datatime: 2023/4/16 17:49

"""
目标: TCP协议实现和多个客户端之间的通信
"""

import socket
import struct # 将 1 ～ 2^31次方范围内的数值转换成4个字节

sk = socket.socket()
sk.bind(('192.168.0.103', 8083))    # 申请操作系统资源
sk.listen()                         # 监听服务

# 方便和多个客户端通信
conn, addr = sk.accept()        # 服务端进行三次握手


sk.close()


