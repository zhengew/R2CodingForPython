# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 子进程绑定方法传递参数.py
# @datatime: 2023/4/27 下午4:02

"""
目标：给子进程绑定方法传参
"""
from multiprocessing import Process
import os
def func1(*args):
    name, age, sex = args
    print(name, age, sex)

if __name__ == '__main__':
    Process(target=func1, args=('alex', 18, 'male')).start() # 子进程绑定方法传参