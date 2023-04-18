# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_解决粘包.py
# @datatime: 2023/4/18 07:28
import socket
import struct

sk = socket.socket()
server = ('192.168.0.103', 8086)
sk.connect(server)

while True:
    # 自定义协议：通过struct模块设置边界
    send_msg = input('>>>').strip()
    send_byte_length = struct.pack('i', len(send_msg.encode('utf-8')))
    print(send_byte_length)
    sk.send(send_byte_length)
    sk.send(send_msg.encode('utf-8'))

    recv_byte_length = struct.unpack('i', sk.recv(4))[0]
    recv_msg = sk.recv(recv_byte_length).decode('utf-8')
    print(recv_msg)


sk.close()