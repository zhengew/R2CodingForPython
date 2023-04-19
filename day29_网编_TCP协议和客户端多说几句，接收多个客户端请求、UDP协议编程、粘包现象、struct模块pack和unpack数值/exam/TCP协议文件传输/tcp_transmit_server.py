# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: tcp_transmit_server.py
# @datatime: 2023/4/19 下午1:35

"""
目标: 基于tcp协议的文件上传和下载
"""

import socket
import struct
import pickle
import os


sk = socket.socket()
sk.bind(('127.0.0.1', 8083))
sk.listen()
def download(path):
    conn, addr = sk.accept()
    print(conn)
    f_len = struct.unpack('i', conn.recv(4))[0]
    filename = conn.recv(f_len).decode('utf-8')
    print(filename)
    path = os.path.join('db_back', filename)
    with open(path, mode='wt', encoding='utf-8') as f:
        while True:
            recv_length = struct.unpack('i', conn.recv(4))[0]
            if recv_length == -1: break
            recv_line = pickle.loads(conn.recv(recv_length))
            f.write(recv_line)

    conn.close



if __name__ == '__main__':
    download(path='./db_back')