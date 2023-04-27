# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 同步阻塞demo.py
# @datatime: 2023/4/27 07:49

"""
目标：理解同步阻塞
执行A事儿的时候触发了B事件，要等待B事件的计算结果才能继续计算A事件，中途有IO操作
"""

a = 1
b = int(input('请输入:')) # 阻塞事件
def add(a, b):
    return a + b

c = add(a, b)

d = a + b + c # 同步阻塞: 在计算d时，需要等待a,b,c的结果，中途在b中遇到的IO操作 input
print(d)