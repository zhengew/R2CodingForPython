# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: tcp_transmit_server.py
# @datatime: 2023/4/19 下午1:35

"""
目标: 基于tcp协议的文件上传和下载
1.客户端需登录认证
2.完成上传和下载功能
3.客户下载时需校验hash值
"""
import logging
logging.basicConfig(level=logging.DEBUG)
import socket
import struct
import json
import hmac
import os
from commons import *
class TransmitServer(object):
    sk = socket.socket()
    server = ('192.168.0.103', 8081)
    sk.bind(server)
    sk.listen()
    users_path = r'./db/userinfo' # 存储已注册用户信息
    login_status = {'login_name': None, 'status': False}

    def register(self, user_dict: dict):
        """
        用户注册
        已注册的用户信息 {'name': 'axle', 'pwd_md5': xxx}...
        :param user: 客户端传输的用户信息 {'name': 'axle', 'pwd_md5': xxx}
        :return: 0-用户已注册， 1-用户注册成功
        """
        # 用户已注册，返回False
        for user in Commons.pickle_load(self.users_path):
            if user_dict['name'] == user['name']:
                return 0
        # 用户未注册，注册信息写入用户文件，返回True
        Commons.pickle_dump(self.users_path, user_dict)
        return 1

    def login(self, login_info: dict):
        """
        客户端登录
        :param login_info: 登录用户 {'login_name': 'alex', 'pwd_md5': md5加密的hash值}
        :return: 登录状态 True/False
        """
        login_name = login_info['login_name']
        login_pwd = login_info['pwd_md5']

        for user in Commons.pickle_load(self.users_path):
            if user['name'] == login_name and user['pwd_md5'] == login_pwd:
                self.login_status['login_name'] = login_name
                self.login_status['status'] = True
                logging.debug(f"login_status:{self.login_status}")
                break
        return self.login_status['status'] # 返回登录状态

    @classmethod
    def download(cls):
        print('in server download')

    @classmethod
    def upload(cls):
        print('in server upload')

    @classmethod
    def exit(cls):
        cls.login_status['login_name'] = None
        cls.login_status['status'] = False
        return True

    @classmethod
    def run(cls):
        while True:
            s = cls()
            s.conn, _ = cls.sk.accept()
            logging.debug(f'当前链接客户端:{s.conn}')
            # 服务端接收客户端送的登录用户信息,并发送登录认证结果
            login_info_blen = struct.unpack('i', s.conn.recv(4))[0]
            login_info = json.loads(s.conn.recv(login_info_blen).decode('utf-8'))
            status = 1 if s.login(login_info) else 0
            s.conn.send(struct.pack('i', status))
            # 登录成功或失败后的逻辑
            logging.debug(f"当前登录用户:{cls.login_status}")
            if s.login_status['status']:
                while True:
                    # 接收客户端要执行的函数名
                    func_name_blen = struct.unpack('i', s.conn.recv(4))[0]
                    func_name = s.conn.recv(func_name_blen).decode('utf-8')
                    # 服务端的上传和下载时反着的
                    if func_name == 'download':
                        func_name = 'upload'
                    elif func_name == 'upload':
                        func_name = 'download'
                    # 反射函数
                    if hasattr(cls, func_name):
                        func = getattr(cls, func_name)
                        if callable(func):
                            if func():
                                break
            logging.debug(f"用户退出登录:{cls.login_status}")
            logging.debug(f'验证客户端断开链接:{s.conn}')
            s.conn.close()
            logging.debug(f'验证客户端断开链接:{s.conn}')

if __name__ == '__main__':
    TransmitServer.run()

    # print(b'0')
    # flag = 1
    # r1 = struct.pack('i', flag)
    # r2 = struct.unpack('i', r1)[0]
    #
    # if r2:
    #     print(len(r1))
    #     print(1111)
    # else:
    #     print(len(r1))
    #     print(2222)
    pwd = hmac.new(key='alex'.encode('utf-8'), msg='123456'.encode('utf-8'), digestmod='md5').hexdigest()
    alex = {'name': 'alex', 'pwd_md5': pwd}
    path = 'db/userinfo'
    # Commons.pickle_dump(path,alex)

    for user in Commons.pickle_load(path):
        print(user)
        print(user['name'])








