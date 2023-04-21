# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: tcp_transmit_client.py
# @datatime: 2023/4/19 下午1:35

"""
目标:文件传输客户端
"""
import socket
import struct
import json
import os
import hmac

class TransmitClient(object):

    __server = ('127.0.0.1', 8085)
    __db_path = r'/home/zew/WeChatFiles/files/backup'
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(self.__server)
    def upload(self, filepath):
        """
        客户端文件上传
        :return:
        """
        if os.path.exists(filepath) and os.path.isfile(filepath):
            filename = os.path.basename(filepath)
            filesize = os.path.getsize(filepath)
            file_info = {'filename': filename, 'filesize': filesize}
            file_info_byte = json.dumps(file_info).encode('utf-8')
            self.sk.send(struct.pack('i',len(file_info_byte)))
            self.sk.send(file_info_byte)
            # 开始上传文件
            file_hash = hmac.new(key=filename.encode('utf-8'), digestmod='md5')
            with open(filepath, mode='rb') as f:
                while filesize > 0:
                    content = f.read(1024)
                    filesize -= len(content)
                    self.sk.send(struct.pack('i', len(content))) # 先发送长度
                    self.sk.send(content)
                    file_hash.update(content)
                f.close()
                file_hash = file_hash.digest() # 上传文件的hash值
                self.sk.send(file_hash)
            print(f'文件[{filename}]已上传至服务器～')
        else:
            print(f"{filepath}文件或路径不存在～")

    def download(self):
        """
        客户端下载服务端的文件
        :return:
        """
        file_list_len = struct.unpack('i', self.sk.recv(4))[0]
        file_list = json.loads(self.sk.recv(file_list_len).decode('utf-8')) # 文件列表
        print(file_list)
        while True:
            for id, file in enumerate(file_list, 1):
                print(f"{id}: {file}")
            index = input('请输入需要下载的文件序号: ')
            if index.isdigit():
                index = int(index)
                if 1 <= index <= len(file_list):
                    index -= 1
                    print(index)
                    self.sk.send(struct.pack('i', index)) # 像服务端传输需要下载的文件列表索引值
                    filesize_len = struct.unpack('i', self.sk.recv(4))[0]
                    filesize = json.loads(self.sk.recv(filesize_len).decode('utf-8')) # 文件md5值和size
                    # 开始下载文件
                    filename = file_list[index-1]
                    abs_filepath = os.path.join(self.__db_path, filename)
                    md5_value = hmac.new(key=filename.encode('utf-8'), digestmod='md5')
                    with open(abs_filepath, mode='wb') as f:
                        while filesize > 0:
                            # content_len = struct.unpack('i', self.sk.recv(4))[0]
                            content = self.sk.recv(1024)
                            f.write(content)
                            filesize -= len(content)
                            md5_value.update(content)
                        f.close()
                    md5_value = md5_value.digest()
                    if md5_value:
                        print(f"文件[{filename}]下载成功，文件md5校验通过")
                    else:
                        print(f"文件[{filename}]下载成功，文件md5校验不通过")

                else:
                    print(f'请输入1~{len(file_list)}之间的数字～')
            else:
                print(f'请输入1~{len(file_list)}之间的数字～')

if __name__ == '__main__':
    path = '/home/zew/WeChatFiles/files/backup/我的自学编程之路.pdf' # 我的自学编程之路.pdf  埋点_20230130.xlsx
    # TransmitClient().upload(path)
    # /Users/erwei.zheng/Downloads/test_download_mail/pycharm-community-2023.1.dmg
    # /Users/erwei.zheng/Downloads/test_download_mail/pytest.pdf
    obj = TransmitClient()
    while True:
        obj.upload(path)
        while True:
            obj.download()