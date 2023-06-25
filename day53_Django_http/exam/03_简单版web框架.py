# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 03_简单版web框架.py
# @datatime: 2023/6/25 下午2:26

import socket

server = socket.socket()
ip_port = ("127.0.0.1", 9000)
server.bind(ip_port)
server.listen()

while True:
    conn, addr =  server.accept()
    from_client_msg = conn.recv(1024)
    print(from_client_msg.decode('utf-8'))
    conn.send(b"HTTP/1.1 200 SUCCESS\r\nUSERNAME:zew\r\nPASSWORD:123\r\n\r\n")

    with open('03_简单版web框架.html', 'rb') as f:
        data = f.read()
    conn.send(data)

    conn.close()