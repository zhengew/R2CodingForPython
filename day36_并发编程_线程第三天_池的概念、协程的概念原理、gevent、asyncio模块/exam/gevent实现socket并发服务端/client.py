# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client.py
# @datatime: 2023/5/3 16:29

"""
目标: socket 客户端
"""

import socket
import time
from threading import Thread

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

def talk(sk):
    while True:
        sk.send(b'hello')
        time.sleep(1)
        msg = sk.recv(1024).decode('utf-8')
        print(msg)

if __name__ == '__main__':
    for i in range(500):
        Thread(target=talk, args=(sk,)).start() # 起500个线程模拟并发
