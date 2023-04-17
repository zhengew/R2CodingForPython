
# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_demo1.py
# @datatime: 2023/4/16 17:49

"""
目标: TCP协议实现和多个客户端之间的通信
"""

import socket

sk= socket.socket() # 创建socket对象
sk.bind(('192.168.0.103', 9094))
sk.listen()

while True: # 实现与多个客户端通信
    conn, addr = sk.accept() # 客户端进行三次握手
    print(conn)
    while True:
        msg = conn.recv(1024)
        if msg.decode('utf-8').upper() == 'Q':
            break
        print(msg.decode('utf-8'))
        send_msg = input('>>>>').strip()
        conn.send(send_msg.encode('utf-8'))
        if send_msg.upper() == 'Q':
            break
    conn.close() # 四次挥手

sk.close()




