# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: server_demo3.py
# @datatime: 2023/4/24 下午2:53

"""
练习3:tcp协议实现一个并发的socket server密文登录
"""
import logging
import socketserver
import hmac
import json
import struct
from commons import Commons

logging.basicConfig(level=logging.DEBUG)


class Transmit(socketserver.BaseRequestHandler):

    __public_key = '我爱你中国'
    __private_key = "我爱你中国"
    __users_path = 'userinfo' # 用户信息存储文件
    def handle(self):
        conn = self.request
        print(conn)
        self.login(conn)

    @classmethod
    def login(cls, conn):
        """
        登陆认证，认证方法 private_key + 客户端md5_pwd 二次加密后比对
        :param conn:当前连接的客户端
        :return: 1-认证通过 0-认证失败
        """
        login_info_blen = struct.unpack('i', conn.recv(4))[0]
        login_info = json.loads(conn.recv(login_info_blen).decode('utf-8'))
        logging.debug(f"登陆用户信息:{login_info}")

        for user in Commons.get_all_users(cls.__users_path):
            if user['name'] == login_info['login_name']:
                if user['pwd'] == Commons.get_md5(cls.__private_key, login_info['pwd']):



        conn.send(b'hello')


if __name__ == '__main__':
    # 启动服务
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9008), Transmit)
    server.serve_forever()
    # md5_pwd = hmac.new(key='我爱你中国'.encode('utf-8'), msg='123456'.encode('utf-8'),digestmod='md5').hexdigest()
    # print(md5_pwd) # 049d6f47236046cc0a06b022a638202d
    #
    # new_pwd = hmac.new(key='我爱你中国'.encode('utf-8'), msg='049d6f47236046cc0a06b022a638202d'.encode('utf-8'), digestmod='md5').hexdigest()
    # print(new_pwd) # c45c484aea5abb4dd212961d5bc44164

