# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 异步阻塞获取进程池返回值.py
# @datatime: 2023/5/3 10:35

"""
目标:通过回掉函数异步阻塞获取函数返回值
"""
from concurrent.futures import ProcessPoolExecutor
from threading import current_thread
import time

def func(*args):
    print(current_thread().name, 'start')
    a, b = args
    time.sleep(0.2)
    return a * b

def print_func(ret): # 回掉函数  异步阻塞执行
    print(ret.result())

if __name__ == '__main__':
    tp = ProcessPoolExecutor(2)
    for i in range(4): # 异步非阻塞 执行进程
        ret = tp.submit(func, i, i+1)
        ret.add_done_callback(print_func) # 绑定回掉函数

