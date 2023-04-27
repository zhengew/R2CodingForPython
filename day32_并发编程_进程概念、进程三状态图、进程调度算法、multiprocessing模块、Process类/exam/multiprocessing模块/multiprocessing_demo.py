# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: multiprocessing_demo.py
# @datatime: 2023/4/25 22:10

"""
目标：multiprocessing模块  多元的处理进程的模块
"""

from multiprocessing import Process
import os

def func():
    print(f'子进程:{os.getpid()}, 父进程:{os.getppid()}')

if __name__ == '__main__':
    print('main:', os.getpid(), os.getppid())
    p = Process(target=func)
    p.start()

"""
main: 15632 28982
子进程:15634, 父进程:15632
"""