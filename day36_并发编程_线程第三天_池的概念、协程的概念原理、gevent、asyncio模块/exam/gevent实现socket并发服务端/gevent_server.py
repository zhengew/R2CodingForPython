# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: gevent_server.py
# @datatime: 2023/5/3 16:28

"""
目标:基于gevent实现socket的server端，规避recve
"""

import gevent
from gevent import monkey
monkey.patch_all()
import socket


sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

def func(conn): # 将可能出现IO操作的代码放在协程函数中
    while True:
        content = conn.recv(1024).decode('utf-8')
        conn.send(content.upper().encode('utf-8'))

if __name__ == '__main__':
    while True:
        conn,_ = sk.accept()
        gevent.spawn(func, conn) # 协程函数