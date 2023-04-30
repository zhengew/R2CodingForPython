# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 线程demo.py
# @datatime: 2023/4/29 21:13

"""
目标:掌握开启线程方式
"""

from threading import Thread
import time

def func(i):
    print('start %s' % i)
    time.sleep(1)
    print('end %s' % i)

if __name__ == '__main__':
    for i in range(5):
        Thread(target=func, args=(i, )).start()