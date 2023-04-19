# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: tcp_transmit_client.py
# @datatime: 2023/4/19 下午1:35
import os.path
import socket
import struct
import pickle


sk = socket.socket()
server = ('127.0.0.1', 8083)

filepath = 'db/test.txt'
def upload(path):
    sk.connect(server)
    filename = os.path.basename(filepath)
    print(filename)
    print(f"开始上传文件{filename}～")
    sk.send(struct.pack('i', len(filename.encode('utf-8'))))
    sk.send(filename.encode('utf-8'))
    with open(filepath, mode='r', encoding='utf-8') as f:
        for line in f:
            send_length = struct.pack('i', len(pickle.dumps(line)))
            sk.send(send_length)
            sk.send(pickle.dumps(line))
        sk.send(struct.pack('i', -1))
    print(f"<<{filename}>>上传完毕~")
    sk.close()

if __name__ == '__main__':
    upload(filepath)


