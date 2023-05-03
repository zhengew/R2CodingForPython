# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 协程demo.py
# @datatime: 2023/5/2 10:49
import gevent
from gevent import monkey
monkey.patch_all()

import time

def func():
    print('in start')
    time.sleep(1)
    print('in end')

g1 = gevent.spawn(func)
g2 = gevent.spawn(func)
g3 = gevent.spawn(func)

gevent.joinall([g1, g2, g3])