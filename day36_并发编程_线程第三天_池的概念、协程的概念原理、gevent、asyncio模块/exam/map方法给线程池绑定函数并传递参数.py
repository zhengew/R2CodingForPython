# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: map方法给线程池绑定函数并传递参数.py
# @datatime: 2023/5/3 08:47

"""
目标: 掌握通过map方法给线程池绑定函数、传参、获取返回值
map方法第一个参数绑定线程要执行的函数，第二个参数接收一个可迭代对象
map的返回值是一个generator生成器对象，通过for/list/next方法获取函数返回值
"""
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time

def func(args):
    print(current_thread().name, 'start')
    time.sleep(1)
    print(current_thread().name, 'end~')
    return args[0] * args[1]

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)
    ret = tp.map(func, [(i, i+1) for i in range(5)])
    print(ret) # <generator object Executor.map.<locals>.result_iterator at 0x1081e6f80>

    print(list(ret)) # [0, 2, 6, 12, 20]






















