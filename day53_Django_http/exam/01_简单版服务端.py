# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 01_简单版web框架.py
# @datatime: 2023/6/25 下午1:20

import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 9001)
sk.bind(ip_port)
sk.listen()

while True:
    conn, addr = sk.accept()
    from_client_msg = conn.recv(1024)
    print(from_client_msg.decode('utf-8'))
    conn.send(b'HTTP/1.1 200 SUCCESS\r\nusername:zew\r\npassword:123\r\n\r\n')

    with open('01_简单版web框架.html', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


