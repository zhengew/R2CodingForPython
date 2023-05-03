# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 后进先出队列.py
# @datatime: 2023/5/1 14:24

"""
目标:掌握后进先出队列(栈)的用法
"""

from queue import LifoQueue

q = LifoQueue()
q.put(1)
q.put(2)
q.put(3)
for i in range(3):
    print(q.get(), end=' ') # 3 2 1   后进来的先出去