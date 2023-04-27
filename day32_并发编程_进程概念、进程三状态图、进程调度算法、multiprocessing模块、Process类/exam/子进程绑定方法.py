# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 子进程绑定方法.py
# @datatime: 2023/4/27 下午3:51

"""
目标：给子进程绑定方法
"""
from multiprocessing import Process
import os
def get_pid():
    print(f"子进程ID:{os.getpid()}, 父进程ID：{os.getppid()}")

if __name__ == '__main__':
    Process(target=get_pid).start()