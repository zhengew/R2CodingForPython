# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: client_demo3.py
# @datatime: 2023/4/24 下午2:54

"""
客户端
"""

import socket
import struct
import hmac
import json
import logging

logging.basicConfig(level=logging.DEBUG)

class TransmitClient(object):
    sk = socket.socket()
    sk.connect(('127.0.0.1', 9008))
    __public_key = '我爱你中国'

    @classmethod
    def login(cls):
        """登陆"""
        login_name = input('用户名:').strip()
        login_pwd = input('密码:').strip()
        md5_pwd = hmac.new(key=cls.__public_key.encode('utf-8'), msg=login_pwd.encode('utf-8'), digestmod='md5').hexdigest()
        login_info = json.dumps({'login_name':login_name, 'pwd':md5_pwd}, ensure_ascii=False)
        login_info_blen = struct.pack('i', len(login_info.encode('utf-8')))
        cls.sk.send(login_info_blen)
        cls.sk.send(login_info.encode('utf-8'))
        logging.debug(f"登陆用户信息{login_info}")
        msg = cls.sk.recv(1024)
        print(msg)
    @classmethod
    def run(cls):
        cls.login()
        cls.sk.close()


if __name__ == '__main__':
    TransmitClient.run()