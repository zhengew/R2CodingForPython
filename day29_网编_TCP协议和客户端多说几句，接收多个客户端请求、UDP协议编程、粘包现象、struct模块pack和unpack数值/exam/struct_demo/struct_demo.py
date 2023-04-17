# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: struct_demo.py
# @datatime: 2023/4/17 22:24

"""
目标: 掌握struct模块的 pack 和 unpack方法
"""

import struct

n1 = 1024
n2 = 15000

# 将数值转换成4位byte类型数值
ret1 = struct.pack('i', n1)
ret2 = struct.pack('i', n2)
print(ret1, len(ret1)) # b'\x00\x04\x00\x00' 4
print(ret2, len(ret2)) # b'\x98:\x00\x00' 4

# 将4位byte类型数据转换成数值,返回值时元组，元组的第一个元素时数值长度
res1 = struct.unpack('i', ret1)
res2 = struct.unpack('i', ret2)
print(res1) # (1024,)
print(res2) # (15000,)
print(type(res1[0])) # <class 'int'>