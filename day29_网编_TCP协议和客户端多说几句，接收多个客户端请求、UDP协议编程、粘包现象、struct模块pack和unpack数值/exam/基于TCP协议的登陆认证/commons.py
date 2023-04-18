# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: commons.py
# @datatime: 2023/4/18 下午3:55

import struct
import pickle

class Commons(object):

    # 测试数据
    __users = {'alex':{'pwd': '123456'}}
    @classmethod
    def login(cls, name, pwd):
        '''
        登陆认证
        :param name:
        :param pwd:
        :return: '1' - 登陆成功， ‘0’ - 登陆失败
        '''
        return '1' if name in cls.__users and pwd == cls.__users[name]['pwd'] else '0'

    @staticmethod
    def get_msg_byte_length(msg: bytes):
        '''
        将字符串encode成字节串，在将字节串的int类型长度用4位字节显示
        :param msg:
        :return: 4位byte类型表示的数值
        '''
        return struct.pack('i', len(msg))

    @staticmethod
    def unpack_msg_byte_length(blen: bytes):
        '''
        将bye类型数值转换成int
        :param blen: 4位字节表示的数值
        :return:
        '''
        return struct.unpack('i', blen)[0]

if __name__ == '__main__':
    ret = Commons.login('alex', '123456')
    print(ret)

    print(Commons.get_msg_byte_length('test1'))
