# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 进程之间数据隔离.py
# @datatime: 2023/4/27 下午4:57

"""
目标:进程之间数据隔离的例子
"""
from multiprocessing import Process
import os
n = 0 # 全局变量n
def func():
    global n
    n += 1
    print(f"{os.getpid()}子进程中全局变量n:{n}") # 子进程与主进程及其他子进程都是数据隔离的
if __name__ == '__main__':
    p_lst = []
    for i in range(2):
        p = Process(target=func)
        p.start() # 异步非阻塞
        p_lst.append(p)
    for p in p_lst:
        p.join() # 同步阻塞
    print(f"{os.getpid()}主进程中全局变量n:{n}")