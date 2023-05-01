# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 通过dis模块解释线程的数据不安全现象.py
# @datatime: 2023/5/1 11:05

"""
目标:通过dis模块的dis函数了解线程的不安全现象
dis.dis() : 显示函数的底层运算逻辑
"""

from dis import dis
a = 0
def func():
    global a
    a += 1

print(dis(func))

