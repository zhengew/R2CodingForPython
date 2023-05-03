# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 回掉函数异步阻塞获取线程池结果.py
# @datatime: 2023/5/2 17:32

"""
目标:掌握线程池中的回掉函数，异步获取线程池返回的future对象
线程池中的线程绑定回掉函数，会在线程返回执行结果时立即调用回掉函数来处理数据，这个过程时异步阻塞的
"""

from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time
def func(a, b):
    print(current_thread().name, 'start')
    time.sleep(1)
    print(current_thread().name, 'end~')
    return {a: a*b}

def print_func(ret): # 异步阻塞
    """回掉函数"""
    print(ret.result())

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)

    for i in range(8):  # 异步非阻塞
        ret = tp.submit(func, i, i+1)
        # ret这个任务会在执行完毕的瞬间立即触发print_func函数，并且把任务的返回值future对象传递到print_func做参数
        ret.add_done_callback(print_func)
        # 异步阻塞： 回掉函数 给ret对象绑定一个回掉函数，等待ret对应的任务有了结果之后立即调用print_func这个函数，
        # 就可以对结果理解进行处理，而不用按照顺序接收结果处理结果