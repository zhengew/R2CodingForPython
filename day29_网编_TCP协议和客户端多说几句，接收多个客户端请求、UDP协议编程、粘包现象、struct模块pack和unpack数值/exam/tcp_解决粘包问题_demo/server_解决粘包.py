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

sk = socket.socket()
sk.bind(('192.168.0.103', 8086))
sk.listen()

while True:
    conn, addr = sk.accept()
    print(conn)
    while True:
        # 服务端接收客户端发送的自定义协议字节长度(unpack回来的元组第一元素)
        recv_byte_length = struct.unpack('i', conn.recv(4))[0]
        print(recv_byte_length)
        recv_msg = conn.recv(recv_byte_length)
        print(recv_msg.decode('utf-8'))

        send_msg = input('>>>').strip()
        send_byte_length = struct.pack('i', len(send_msg.encode('utf-8')))
        conn.send(send_byte_length)
        conn.send(send_msg.encode('utf-8'))

    conn.close()

sk.close()

