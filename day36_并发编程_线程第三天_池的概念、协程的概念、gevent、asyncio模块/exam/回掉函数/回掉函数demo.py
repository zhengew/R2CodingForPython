# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 回掉函数demo.py
# @datatime: 2023/5/1 16:46

"""
目标:回掉函数demo
"""

from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time, random


def func(a, b):
    print(current_thread().name, 'start', a, b)
    time.sleep(random.randint(1, 4))
    print(current_thread().name, 'end')
    return a * b

def print_func(ret):
    print(ret.result())

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)
    for i in range(4):
        ret = tp.submit(func, i, b = i+1)
        ret.add_done_callback(print_func)  # 回掉函数会异步阻塞的执行，拿到ret结果就立马执行回到函数 print_func



