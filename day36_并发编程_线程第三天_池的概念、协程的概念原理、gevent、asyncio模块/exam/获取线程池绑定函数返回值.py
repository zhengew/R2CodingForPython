# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 获取线程池绑定函数返回值.py
# @datatime: 2023/5/2 16:53

"""
目标:获取线程池绑定函数返回值
线程池绑定函数的返回值是个future类对象，通过调用 result方法来获取最终函数返回值；
"""
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time
def func(a:int, b:int):
    print(current_thread().name)
    time.sleep(1)
    return {a: a*b}

if __name__ == '__main__':
    tp = ThreadPoolExecutor(2)
    ret_lst = []
    for i in range(4):
        ret = tp.submit(func, i, i+1) # 异步非阻塞
        ret_lst.append(ret)

    for ret in ret_lst: # 同步阻塞 打印线程返回值结果，因为ret是按照顺序添加到ret_lst中的，所以是同步阻塞
        print(ret.result())