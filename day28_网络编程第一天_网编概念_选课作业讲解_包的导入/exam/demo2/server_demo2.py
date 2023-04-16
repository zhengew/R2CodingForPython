# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_demo2.py
# @datatime: 2023/4/15 21:45

import socket

sk = socket.socket()                # 创建一个server端对象
sk.bind(('127.0.0.1', 8080))        # 给server端绑定地址和端口
sk.listen()                         # 开始监听(可以接收)客户端给我的链接了



while True:
    conn, addr = sk.accept()        # 建立连接, conn 是链接
    msg = conn.recv(1024)
    print(msg)
    conn.send(b'hello')
    conn.close()                    # 关闭链接

sk.close()                          # 关闭整个服务