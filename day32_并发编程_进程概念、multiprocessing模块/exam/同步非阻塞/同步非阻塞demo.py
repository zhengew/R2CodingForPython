# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 同步非阻塞demo.py
# @datatime: 2023/4/27 07:42

"""
目标：理解同步非阻塞
执行A事儿的时候触发了B事件，要等待B事件的计算结果才能继续计算A事件，且全程没有IO操作
"""

a = 1
b = 2

def add(a, b):
    return a + b

c = add(a, b)

d = a + b + c # 同步非阻塞: 在计算d时 需要等待c的结果才能拿到d的结果，且全程都没有IO操作
print(d)