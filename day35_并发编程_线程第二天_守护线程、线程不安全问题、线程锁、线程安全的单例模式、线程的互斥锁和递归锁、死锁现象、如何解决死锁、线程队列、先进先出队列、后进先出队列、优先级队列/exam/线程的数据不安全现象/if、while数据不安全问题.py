# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: if、while数据不安全问题.py
# @datatime: 2023/5/1 11:19

"""
目标:理解为什么if/while会出现线程间数据不安全问题
"""
from threading import Thread
from queue import Queue
from dis import dis

q = Queue()

def consumer(q):
    while True:
        ret = q.get()
        if ret:
            print(ret, end=' ')
        else:
            break

def producter(q):
    for i in range(10):
        q.put('-->%s'%i)

if __name__ == '__main__':
    p1 = Thread(target=producter, args=(q,))
    p1.start()

    c1 = Thread(target=consumer, args=(q,))
    c1.start()
    p1.join()
    q.put(None)


