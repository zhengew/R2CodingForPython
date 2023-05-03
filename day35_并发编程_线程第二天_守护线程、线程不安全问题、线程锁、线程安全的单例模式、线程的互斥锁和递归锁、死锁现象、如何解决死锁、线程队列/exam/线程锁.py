# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 线程锁.py
# @datatime: 2023/5/1 12:35

"""
目标: 通过加线程锁解决线程数据安全问题
"""
from threading import Thread, Lock
import time
def append():
    for i in range(50000):
        n.append(i)
def pop(lock):
    for i in range(50000):
        with lock: # 互斥锁
            if not n:
                time.sleep(0.0000000001) # 强制列表为空时进行CPU时间片轮转，这样在pop时可能会出现Empty异常
            n.pop()

if __name__ == '__main__':
    n = []
    lock = Lock() # 互斥锁
    t_lst = []
    for i in range(2):
        t1 = Thread(target=append)
        t1.start()
        t2 = Thread(target=pop, args=(lock,))
        t2.start()
        t_lst.append(t1)
        t_lst.append(t2)
    for t in t_lst: t.join()
    print(n)