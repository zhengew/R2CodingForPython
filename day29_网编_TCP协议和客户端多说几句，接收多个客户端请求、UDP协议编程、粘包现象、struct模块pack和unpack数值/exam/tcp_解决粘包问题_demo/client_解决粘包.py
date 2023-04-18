# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_解决粘包.py
# @datatime: 2023/4/18 07:28
import socket
import struct

sk = socket.socket()                    # 创建socket对象
server = ('127.0.0.1', 8087)            # 服务端 ip和端口
sk.connect(server)                      # 与服务端进行三次握手

while True:
    # 自定义协议：通过struct模块设置边界
    send_msg = input('>>>').strip()
    # 将消息编码成字节串并计算字节长度，再将字节长度转换成4个字节表示的数值
    send_byte_length = struct.pack('i', len(send_msg.encode('utf-8')))
    print(send_byte_length)
    sk.send(send_byte_length)           # 自定义协议，约定客户端发送消息的长度，避免黏包
    sk.send(send_msg.encode('utf-8'))
    if send_msg.upper() == 'Q':
        break

    # 接收服务端发送的消息（自定义协议）
    recv_byte_length = struct.unpack('i', sk.recv(4))[0]
    recv_msg = sk.recv(recv_byte_length).decode('utf-8')
    if recv_msg.upper() == 'Q':
        break
    print(recv_msg)

sk.close()                              # 客户端进行四次挥手