# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 开启多个子进程.py
# @datatime: 2023/4/27 下午4:22

"""
目标:开启多个子进程
"""

from multiprocessing import Process
import sys
def func():
    print(id(func))

if __name__ == '__main__':
    for i in range(4): # 开启多个子进程
        p = Process(target=func)
        p.start()