# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 04_升级版web框架.py
# @datatime: 2023/6/25 下午3:23

import socket

server = socket.socket()
ip_port = ("127.0.0.1", 8081)
server.bind(ip_port)
server.listen()

while True:
    conn, addr =  server.accept()
    from_client_msg = conn.recv(1024).decode('utf-8')
    # print(from_client_msg.decode('utf-8'))
    path = from_client_msg.split('\r\n')[0].split(' ')[1]
    print(path)
    conn.send(b"HTTP/1.1 200 SUCCESS\r\nUSERNAME:zew\r\nPASSWORD:123\r\n\r\n")

    match path:
        case '/':
            with open('04_升级版web框架.html', 'rb') as f:
                data = f.read()
            conn.send(data)
        case '/day53.css':
            with open('day53.css', 'rb') as f:
                data = f.read()
            conn.send(data)
        case '/background-img.png':
            with open('background-img.png', 'rb') as f:
                data = f.read()
            conn.send(data)
        case '/day53.js':
            with open('day53.js', 'rb') as f:
                data = f.read()
            conn.send(data)
        case '/myicon.ico':
            with open('myicon.ico', 'rb') as f:
                data = f.read()
            conn.send(data)
        case _:
            conn.send(b'HTTP/1.1 404 not fond/r/n/r/n')

    conn.close()