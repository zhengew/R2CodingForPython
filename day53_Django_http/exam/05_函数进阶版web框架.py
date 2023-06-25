# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 05_函数进阶版web框架.py
# @datatime: 2023/6/25 19:56

import socket

server = socket.socket()
ip_port = ('127.0.0.1', 8081)
server.bind(ip_port)
server.listen()

def html():
    with open('05_函数进阶版web框架.html', 'rb') as f:
        data = f.read()
    return data

def css():
    with open('day53.css', 'rb') as f:
        data = f.read()
    return data
def js():
    with open('day53.js', 'rb') as f:
        data = f.read()
    return data
def icon():
    with open('myicon.ico', 'rb') as f:
        data = f.read()
    return data
def img():
    with open('background-img.png', 'rb') as f:
        data = f.read()
    return data

while True:
    conn, addr = server.accept()
    from_client_msg = conn.recv(1024).decode('utf-8')
    path = from_client_msg.split('\r\n')[0].split(' ')[1]
    print(path)
    conn.send(b'HTTP/1.1 200 SUCCESS\r\n\r\n')

    match path:
        case '/':
            data = html()
        case '/day53.css':
            data = css()
        case '/background-img.png':
            data = img()
        case '/day53.js':
            data = js()
        case '/myicon.ico':
            data = icon()
        case _:
            conn.send(b'HTTP/1.1 404 not fond/r/n/r/n')

    conn.send(data)

    conn.close()