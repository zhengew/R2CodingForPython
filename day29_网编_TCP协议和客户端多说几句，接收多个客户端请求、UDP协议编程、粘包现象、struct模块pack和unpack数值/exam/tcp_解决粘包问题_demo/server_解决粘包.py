# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_解决粘包.py
# @datatime: 2023/4/18 07:28

"""
目标: 掌握如何解决TCP协议粘包问题
1.粘包问题出现的原因: TCP协议的流式传输导致
2.如何解决：设置每次传输的边界
3.通过struct模块的pack、unpack方法设置边界，
注意：计算的是字符串的字节长度，不是字符串长度
"""
import socket
import struct

sk = socket.socket()                            # 创建socket对象
sk.bind(('127.0.0.1', 8087))                    # 服务端申请系统资源 绑定端口
sk.listen()                                     # 监听服务

while True:
    conn, addr = sk.accept()                    # 服务端三次握手
    print(conn)
    while True:                                 # 服务端接收和发送消息
        # 服务端接收客户端发送的自定义协议字节长度(unpack回来的元组第一元素)
        recv_byte_length = struct.unpack('i', conn.recv(4))[0]  # 接收客户端自定义协议的字节串长度，并unpack回来，取返回值元组的第0个元素
        print(recv_byte_length)
        recv_msg = conn.recv(recv_byte_length) # 接收客户端发送的指定长度的字节串
        if recv_msg.decode('utf-8').upper() == 'Q':
            break
        print(recv_msg.decode('utf-8'))

        # 服务端向客户端发送消息，先发送消息字节串长度再发编码后的消息
        send_msg = input('>>>').strip()
        send_byte_length = struct.pack('i', len(send_msg.encode('utf-8')))
        conn.send(send_byte_length)
        conn.send(send_msg.encode('utf-8'))
        if send_msg.upper() == 'Q':
            break

    conn.close()                                # 服务端进行四次挥手

sk.close()                                      # 关闭服务端

