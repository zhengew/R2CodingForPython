# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 先进先出队列.py
# @datatime: 2023/5/1 14:10

"""
目标: queue模块的先进先出队列
"""
from queue import Queue, Empty, Full

q = Queue(3) # 设置先进先出队列容器大小
q.put(1)
q.put(2)
q.put(3)
try:
    q.put_nowait(4)
except Full:
    print('队列以满')

print(q.get())
print(q.get())
print(q.get())

try:
    print(q.get_nowait())
except Empty:
    pass