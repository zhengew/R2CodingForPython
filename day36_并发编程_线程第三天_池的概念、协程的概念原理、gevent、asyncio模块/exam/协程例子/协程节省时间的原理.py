# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 协程原理.py
# @datatime: 2023/5/3 15:12

"""
目标:演示协程的工作原理
"""
import gevent
from gevent import monkey
monkey.patch_all()
import time

def func1():
    print('start')
    time.sleep(1)
    print('end')

def func2():
    print('start')
    time.sleep(1)
    print('end')

g1 = gevent.spawn(func1)
g2 = gevent.spawn(func2)
gevent.joinall([g1, g2])