# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 池_demo.py
# @datatime: 2023/5/1 16:15

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import current_thread
import time
import random

def func(a, b):
    print(current_thread().ident, 'start', a, b)
    time.sleep(random.randint(1, 4))
    print(current_thread().ident, 'end')

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)
    for i in range(20):
        tp.submit(func, i, b=i+1)