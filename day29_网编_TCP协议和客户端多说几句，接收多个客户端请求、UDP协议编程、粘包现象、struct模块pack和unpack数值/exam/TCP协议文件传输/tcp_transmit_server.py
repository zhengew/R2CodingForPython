# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: tcp_transmit_server.py
# @datatime: 2023/4/19 下午1:35

"""
目标: 基于tcp协议的文件上传和下载
"""

import socket
import struct
import json
import hmac
import os

class TransmitServer(object):

    __server = ('127.0.0.1', 8085)  # 服务端地址
    __dbpath = r'/home/zew/WeChatFiles/files/backup/db_back'   # 服务端存储文件路径
    __dbfiles = dict() # 服务器端存储文件的filename, md5, size
    def __init__(self):
        self.sk = socket.socket()
        self.sk.bind(self.__server)
        self.sk.listen()
        self.conn, _ = self.sk.accept()
    def download(self):
        """
        服务端接收客户端上传的文件
        :return:
        """
        file_info_len = struct.unpack('i', self.conn.recv(4))[0]
        file_info = json.loads(self.conn.recv(file_info_len).decode('utf-8'))
        filename = file_info['filename']
        filesize = file_info['filesize']
        abs_filepath = os.path.join(self.__dbpath, filename) # 服务器保存的绝对路径
        print(filename, filesize, type(filesize))
        with open(abs_filepath, mode='wb') as f:
            while filesize > 0:
                content_len = struct.unpack('i', self.conn.recv(4))[0]
                content = self.conn.recv(content_len)
                f.write(content)
                filesize -= len(content)
            f.close()

        file_hash = self.conn.recv(16) # byte类型在给客户端传输md5值是会json序列化失败
        TransmitServer.__dbfiles[filename] = {'md5':file_hash, 'size': file_info['filesize']}
        print(self.__dbfiles[filename])
        print(f'文件[{filename}]已接收完毕～')

    def upload(self):
        """
        服务端提供下载文件功能
        向服务端发送可下载的文件名
        :return:
        """
        # 文件列表，忽略隐藏文件，按字母顺序正序排列
        file_lst = sorted([f for f in os.listdir(self.__dbpath) if not f.startswith('.')], key=lambda f: f.lower())
        print(file_lst)
        file_lst_byte = json.dumps(file_lst).encode('utf-8')
        self.conn.send(struct.pack('i', len(file_lst_byte))) # 文件列表的字节长度
        self.conn.send(file_lst_byte)
        file_index = struct.unpack('i', self.conn.recv(4))[0] # 客户端需要下载的文件名下标
        print(f"file_index: {file_index}")
        file_abs_path = os.path.join(self.__dbpath, file_lst[file_index]) # 客户端需要下载的文件的绝对路径
        print(file_abs_path)
        # 需要给客户端传输一个文件的hash值，验证数据完整性；在去发送文件
        print(self.__dbfiles)
        filename = file_lst[file_index]
        file_size = json.dumps(self.__dbfiles[filename]['size']).encode('utf-8')
        print(file_size)
        self.conn.send(struct.pack('i', len(file_size)))
        self.conn.send(file_size) # 向客户端传输文件md5值和size
        # 开始上传文件
        filesize = self.__dbfiles[filename]['size']
        with open(file_abs_path, mode='rb') as f:
            while filesize > 0:
                content = f.read(1024)
                filesize -= len(content)
                # self.sk.send(struct.pack('i', len(content)))  # 先发送长度
                self.sk.send(content)
            f.close()
        print(f'文件[{filename}]传输完毕～')


if __name__ == '__main__':
    obj = TransmitServer()

    while True:
        obj.download()
        while True:
            obj.upload()
