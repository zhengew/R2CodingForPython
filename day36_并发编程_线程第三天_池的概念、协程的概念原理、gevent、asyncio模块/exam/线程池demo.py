# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 线程池demo.py
# @datatime: 2023/5/2 16:19

"""
目标: 掌握如何开启线程池、如何绑定函数、如何传参
"""

from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time
def func(name):
    print(current_thread().name, 'start', name)
    time.sleep(1)
    print(current_thread().name, 'end')

if __name__ == '__main__':
    tp = ThreadPoolExecutor(3)
    tp.submit(func, 'taibai')
    tp.submit(func, 'alex')
    tp.submit(func, name='wusir')



