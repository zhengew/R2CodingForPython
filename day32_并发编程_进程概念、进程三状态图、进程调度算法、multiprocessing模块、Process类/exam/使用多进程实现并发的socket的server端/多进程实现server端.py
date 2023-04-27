# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 多进程实现server端.py
# @datatime: 2023/4/27 下午5:17

"""
目标:使用多进程实现socket的server端
"""
import socket
from multiprocessing import Process
def talk(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        conn.send(msg.upper().encode('utf-8'))
    conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9001))
    sk.listen() # 主进程负责申请服务资源
    while True:
        conn, _ = sk.accept() # 子进程负责接收连接
        Process(target=talk, args=(conn, )).start()
    sk.close()