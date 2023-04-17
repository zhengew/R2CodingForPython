# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_demo2.py
# @datatime: 2023/4/16 18:08

import socket

sk = socket.socket()
sk.bind(('192.168.0.103', 8081))
sk.listen()

while True:
    conn, addr = sk.accept() # 和多个客户端握手
    print(conn)
    msg = conn.recv(1024)
    print(msg)
    conn.send('你好'.encode('utf-8'))
    conn.close()

sk.close()