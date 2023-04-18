# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_demo.py
# @datatime: 2023/4/18 下午12:41

import socket
import struct
import pickle
from commons import Commons

sk = socket.socket()
server = ('127.0.0.1', 8080)
sk.connect(server)

while True:
    login_name = input('请输入登陆用户名: ')
    login_pwd = input('请输入登陆密码: ')
    login_info = {'login_name': login_name, 'login_pwd': login_pwd} # 登陆信息
    login_dict = pickle.dumps(login_info)
    send_length = Commons.get_msg_byte_length(login_dict)
    sk.send(send_length)
    sk.send(login_dict)
    login_state = sk.recv(4).decode('utf-8')
    if login_state == '1':
        print('test 登陆成功')
    else:
        print('用户名或密码错误～')
        break
sk.close()
