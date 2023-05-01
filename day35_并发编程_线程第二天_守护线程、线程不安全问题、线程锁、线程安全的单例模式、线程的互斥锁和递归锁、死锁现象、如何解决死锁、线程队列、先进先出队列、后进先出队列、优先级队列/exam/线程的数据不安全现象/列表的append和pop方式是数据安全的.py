# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 列表的append和pop方式是数据安全的.py
# @datatime: 2023/5/1 11:53

"""
目标:通过dis模块了解为什么列表的append/pop方式是数据安全的
"""

from dis import dis

a = []

def func():
    global a
    a.append(1)

print(dis(func))