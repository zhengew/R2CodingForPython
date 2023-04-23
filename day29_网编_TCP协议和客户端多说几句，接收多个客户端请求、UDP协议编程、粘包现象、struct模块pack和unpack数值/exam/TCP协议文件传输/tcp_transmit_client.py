# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: tcp_transmit_client.py
# @datatime: 2023/4/19 下午1:35

"""
目标:文件传输客户端
1.客户端用户注册功能
    1.用户名
        1>校验用户是否被注册，如已注册，提示用户重新输入
    2.密码: md5加密, hmac模块，key=name, msg=pwd, 加密算法 md5
    3.注册成功，向服务端传输{'name': 'axle', 'pwd_md5': xxx}
    4.返回功能选择页面
2.客户端登录验证：
    1>向服务端传输{'login_name': 'alex', pwd_md5: md5加密的hash值}
    2>如果服务端校验通过，可继续选择其他功能，否则断开连接
3.客户上传文件
    1>客户输入文件路径
    2>传输文件信息的json串{'file_name': 'test.txt', 'size':1000, 'md5_value': xxx}
        2.1> 需要写一个获取md5加密值的函数
4.文件下载
    1>服务端提供可下载的文件列表
        1.1>[文件名1, 文件名2, ....]
    2.服务端提供客户端需下载的文件信息
        2.1>{'file_name: 'test1.txt', 'size': 1000, 'md5_value': xxx}
5.退出登录
    1>客户端断开链接
    2>客户端断开链接时，服务端需要更新用户登录状态
6.用户上传或下载完后，返回功能选择页面
    1>上传文件
    2>下载文件
    3>退出登录


"""
import socket
import struct
import json
import os
import hmac
import logging
logging.basicConfig(level=logging.DEBUG)

class TransmitClient(object):

    sk = socket.socket()
    # sk.connect(('192.168.0.103', 8081))
    __commands = [('注册', 'register'), ('上传', 'upload'), ('下载', 'download'), ('退出', 'exit')]
    __login_name = None
    # __download_path = r'/home/zew/WeChatFiles/files/backup/db_client/'
    __download_path = r'/Users/erwei.zheng/Downloads/test_download_mail/backup_client'

    @staticmethod
    def get_md5(*args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return: md5加密后的hash值，32位的字符串
        """
        name, pwd = args
        return hmac.new(key=name.encode('utf-8'), msg=pwd.encode('utf-8'), digestmod='md5').hexdigest()

    @staticmethod
    def get_file_md5(filename: str, filesize: int, filepath: str):
        """
        待上传文件md5值
        :param path:
        :return: md5值，32位字符串
        """
        h = hmac.new(key=filename.encode('utf-8'), digestmod='md5')
        with open(filepath, mode='rb') as f:
            while filesize > 0:
                content = f.read(1024)
                h.update(content)
                filesize -= len(content)
            f.close()
        return h.hexdigest()


    @classmethod
    def login(cls):
        """
        登录认证 {'login_name': 'alex', pwd_md5: md5加密的hash值}
        :return: 返回值 1-登录成功， 0-登录失败
        """
        login_name = input('用户名:').strip()
        login_pwd = input('密码: ').strip()
        cls.__login_name = login_name # 客户端保存当前登录用户名
        # 向服务端发送登录用户信息
        login_info = {'login_name': login_name, 'pwd_md5': cls.get_md5(login_name, login_pwd)}
        login_info = json.dumps(login_info) # 序列化
        login_info_blen = struct.pack('i', len(login_info.encode('utf-8')))
        cls.sk.send(login_info_blen)
        cls.sk.send(login_info.encode('utf-8'))
        # 接收服务端发送的登录认证结果, 1-成功 2-失败
        return struct.unpack('i', cls.sk.recv(4))[0]

    @classmethod
    def register(cls):
        """注册"""
        name = input('用户名: ').strip()
        pwd = input('密码: ').strip()
        pwd_md5 = hmac.new(key=name.encode('utf-8'), msg=pwd.encode('utf-8'), digestmod='md5').hexdigest()
        # 发送注册用户信息
        user_dict = json.dumps({'name':name, 'pwd_md5':pwd_md5}, ensure_ascii=False)
        user_dict_len = struct.pack('i', len(user_dict.encode('utf-8')))
        cls.sk.send(user_dict_len)
        cls.sk.send(user_dict.encode('utf-8'))
        # 判断是否注册成功，0-注册失败 1-注册成功
        state = struct.unpack('i', cls.sk.recv(4))[0]
        if state:
            print(f"用户{name}注册成功～")
        else:
            print(f"用户{name}已被注册，请更换用户名重新注册～")

    @classmethod
    def upload(cls):
        """
        上传
       {'file_name': 'test.txt', 'size':1000, 'md5_value': xxx}
       /Users/erwei.zheng/Downloads/test_download_mail/backup_client/pycharm-community-2023.1.dmg
        :return:
        """
        try:
            # 待上传的文件信息发送给服务端
            filepath = input('请输入文件绝对路径: ').strip()
            filename = os.path.basename(filepath)
            size = os.path.getsize(filepath)
            logging.debug(f'文件大小:{size}')
            md5_value = cls.get_file_md5(filename, size, filepath)
            file_info = json.dumps({'file_name': filename, 'size':size, 'md5_value': md5_value})
            file_info_blen = struct.pack('i', len(file_info.encode('utf-8')))
            cls.sk.send(file_info_blen)
            cls.sk.send(file_info.encode('utf-8'))
            # 开始上传文件
            with open(filepath, mode='rb') as f:
                while size > 0:
                    content = f.read(2048)
                    size -= len(content)
                    cls.sk.send(content)
                f.close()
            print(f'[{filename}]文件上传完毕～')
        except FileExistsError:
            print(f'[{filename}]文件不存在～')

    @classmethod
    def download(cls):
        """下载"""
        # 接收服务端存储的文件列表
        dbfiles_info_blen = struct.unpack('i', cls.sk.recv(4))[0]
        dbfiles_info = json.loads(cls.sk.recv(dbfiles_info_blen).decode('utf-8'))
        # logging.debug(f"服务端文件下载列表:{dbfiles_info}\n")

        # 客户端传输要下载的文件名
        try:
            files = [file['file_name'] for file in dbfiles_info]
            for id, file in enumerate(files, 1):
                print(f"{id}: {file}")
            index = int(input('请输入要下载的文件ID: ').strip()) - 1
            download_file = dbfiles_info[index]
            download_file_blen = struct.pack('i', len(json.dumps(download_file, ensure_ascii=False).encode('utf-8')))
            cls.sk.send(download_file_blen)
            cls.sk.send(json.dumps(download_file, ensure_ascii=False).encode('utf-8'))
            # 写入文件
            size = download_file['size']
            file_abspath = os.path.join(cls.__download_path, download_file['file_name'])
            m = hmac.new(key=download_file['file_name'].encode('utf-8'), digestmod='md5')
            with open(file_abspath, mode='wb') as f:
                while size > 0:
                    content = cls.sk.recv(2048)
                    size -= len(content)
                    f.write(content)
                    m.update(content)
                f.close()
            # md5校验文件
            md5_value = m.hexdigest()
            logging.debug(f"服务端MD5：{download_file['md5_value']},客户端MD5: {md5_value}")
            if md5_value == download_file['md5_value']:
                print(f'{download_file["file_name"]}文件校验通过，下载完毕')
            else:
                print(f'{download_file["file_name"]}文件校验不通过，请重新下载完毕')
                os.remove(file_abspath)

        except Exception:
            print(f'您要下载的文件不存在～')

    @classmethod
    def exit(cls):
        """退出"""
        print(f'[{cls.__login_name}]退出系统～')
        cls.__login_name = None
        return True

    @classmethod
    def show_commands(cls):
        """
        客户端用户选择功能列表
        :return:
        """
        while True:
            for id, command in enumerate(cls.__commands, 1):
                print(f'{id}: {command[0]}')
            try:
                index = int(input('请选择功能: ').strip()) - 1
                if hasattr(cls, cls.__commands[index][1]):
                    # 把客户端要执行的函数名发送给服务端
                    func_name = cls.__commands[index][1]
                    func_name_blen = struct.pack('i', len(func_name.encode('utf-8')))
                    cls.sk.send(func_name_blen)
                    cls.sk.send(func_name.encode('utf-8'))
                    # 反射函数
                    func = getattr(cls, func_name)
                    if callable(func):
                        if func():
                            break
            except Exception:
                print('您选择的功能不存在，请重新输入～')

    @classmethod
    def run(cls):
        while True:
            cls.sk.connect(('192.168.0.103', 8082))
            if cls.login():
                print(f'欢迎[{cls.__login_name}]登录文件传输平台～')
                cls.show_commands()
                break
            else:
                print('用户名或密码错误～')
                break
        cls.sk.close() # 断开链接

if __name__ == '__main__':
    TransmitClient.run()

    # name = 'pycharm-community-2023.1.dmg'
    # path = r'/Users/erwei.zheng/Downloads/test_download_mail/backup_client/pycharm-community-2023.1.dmg'
    # size = os.path.getsize(path)
    # print(size)
    # m = TransmitClient.get_file_md5(name, size, path)
    # print(m) # 435db82441cb1a0fa0c3b9f7628edcfb