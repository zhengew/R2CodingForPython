# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 优先级队列.py
# @datatime: 2023/5/1 14:30

"""
目标:掌握队列模块中的优先级队列
优先级传参是个元组数据，第1个元素代表优先级，第2个元素代表要传递的数据
"""

from queue import PriorityQueue

q = PriorityQueue()
q.put((0, 'taibai'))
q.put((0, 'alex'))
q.put((1, 'wusir'))
q.put((2, '大壮'))

for i in range(4):
    print(q.get())