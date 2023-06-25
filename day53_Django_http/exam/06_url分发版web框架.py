# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 06_url分发版web框架.py
# @datatime: 2023/6/25 20:11

import socket
from threading import Thread

server = socket.socket()
ip_port = ('127.0.0.1', 8081)
server.bind(ip_port)
server.listen()

def html(conn):
    with open('06_url分发版web框架.html', 'rb') as f:
        data = f.read()
    conn.send(data)

def css(conn):
    with open('day53.css', 'rb') as f:
        data = f.read()
    conn.send(data)
def js(conn):
    with open('day53.js', 'rb') as f:
        data = f.read()
    conn.send(data)
def icon(conn):
    with open('myicon.ico', 'rb') as f:
        data = f.read()
    conn.send(data)
def img(conn):
    with open('background-img.png', 'rb') as f:
        data = f.read()
    conn.send(data)

url_patters = [
    ('/', html),
    ('/day53.css', css),
    ('/day53.js', js),
    ('/background-img.png', img),
    ('/myicon.ico', icon),
]


while True:
    conn, addr = server.accept()
    from_client_msg = conn.recv(1024).decode('utf-8')
    path = from_client_msg.split('\r\n')[0].split(' ')[1]
    print(path)
    conn.send(b'HTTP/1.1 200 SUCCESS\r\n\r\n')

    for i in url_patters:

        if i[0] == path:
            print(i[1])
            t = Thread(target=i[1], args=(conn,))
            t.start()







