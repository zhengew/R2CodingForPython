# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 04_升级版web框架.py
# @datatime: 2023/6/25 下午3:23

import socket

server = socket.socket()
ip_port = ("127.0.0.1", 9001)
server.bind(ip_port)
server.listen()

while True:
    conn, addr = server.accept()
    from_client_msg = conn.recv(1024).decode("utf-8")
    print(from_client_msg)
    path = from_client_msg.split('\r\n')[0].split(' ')[1]
    print(path)
    conn.send(b"HTTP/1.1 200 SUCCESS/r/nusername:zew/r/npassword:123/r/n/r/n")
    if path == "/":
        with open('04升级版web框架.html', 'rb') as f:
            data = f.read()
        conn.send(data)

    conn.close()