# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: login_auth_server.py
# @datatime: 2023/4/18 下午12:41

import socket
import struct
import pickle
from commons import Commons

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

while True:
    conn,_ = sk.accept()
    print(conn)
    while True:
        recv_length = Commons.unpack_msg_byte_length(conn.recv(4))
        recv_msg = conn.recv(recv_length)
        login_info = pickle.loads(recv_msg)
        print(f'登陆信息: {login_info}')
        login_state = Commons.login(login_info['login_name'], login_info['login_pwd'])
        print(f'登陆状态: {login_state}')
        conn.send(login_state.encode('utf-8'))
        if login_state == '0':
            break

    conn.close()

sk.close()