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
from commons import Commons

class TransmitServer(object):
    sk = socket.socket()
    server = ('127.0.0.1', 8084)
    sk.bind(server)
    sk.listen()
    users_path = r'./db/userinfo'       # 存储已注册用户信息
    fileinfo_path = r'./db/fileinfo'    # 存储服务端文件信息
    # file_db_path = r'/Users/erwei.zheng/Downloads/test_download_mail/backup/' # 服务端文件存储路径
    file_db_path = r'/home/zew/WeChatFiles/files/backup/' # 服务端存储文件路径
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

    def download(self):
        """
        服务端接收客户端上传的文件
        :return:
        """
        # 接收客户端待上传的文件信息
        file_info_blen = struct.unpack('i',self.conn.recv(4))[0]
        file_info = json.loads(self.conn.recv(file_info_blen).decode('utf-8'))
        logging.debug(f'客户端上传的文件信息:{file_info}')
        # 将文件信息写入到 ./db/fileinfo,如果存在就更新文件信息
        Commons.update_fileinfo(self.fileinfo_path, file_info)
        # 写入文件
        size = file_info['size']
        file_abspath = os.path.join(self.file_db_path, file_info['file_name'])
        with open(file_abspath, mode='wb') as f:
            while size > 0:
                content = self.conn.recv(2048)
                size -= len(content)
                f.write(content)
            f.close()
        logging.info(f"{file_info['file_name']}文件传输完毕～")

    def upload(self):
        """
        服务端向客户端发送文件
        :return:
        """
        # 向客户端传输服务端存储的文件列表
        dbfiles_info = Commons.get_dbfiles_info(self.fileinfo_path)
        dbfiles_info_blen = struct.pack('i', len(json.dumps(dbfiles_info).encode('utf-8')))
        logging.debug(f"服务端文件下载列表:{dbfiles_info}")
        self.conn.send(dbfiles_info_blen)
        self.conn.send(json.dumps(dbfiles_info).encode('utf-8'))
        # 接收客户要下载的文件信息
        download_file_blen = struct.unpack('i', self.conn.recv(4))[0]
        download_file = json.loads(self.conn.recv(download_file_blen).decode('utf-8'))
        size = download_file['size']
        file_abs_path = os.path.join(self.file_db_path, download_file['file_name']) # 文件绝对路径
        with open(file_abs_path, mode='rb') as f:
            while size > 0:
                content = f.read(1024)
                size -= len(content)
                self.conn.send(content)




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
                    if hasattr(s, func_name):
                        func = getattr(s, func_name)
                        if callable(func):
                            if func():
                                break
            logging.debug(f"用户退出登录:{s.login_status}")
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








