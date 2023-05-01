# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 死锁现象案例_吃面.py
# @datatime: 2023/5/1 13:35

"""
目标:通过吃面案例演示多线程之间的死锁现象
"""
from threading import Thread, Lock
import time
def eat1(name):
    fork_lock.acquire()
    print(name, '抢到叉子～')
    noodle_lock.acquire()
    print(name, '抢到面～')
    print(name, '开始吃面～')
    time.sleep(0.1)
    noodle_lock.release()
    print(name,'放下面~')
    fork_lock.release()
    print(name, '放下叉子')
def eat2(name):
    noodle_lock.acquire()
    print(name, '抢到面～')
    fork_lock.acquire()
    print(name, '抢到叉子～')
    print(name, '开始吃面～')
    time.sleep(0.1)
    fork_lock.release()
    print(name, '放下叉子')
    noodle_lock.release()
    print(name,'放下面~')

if __name__ == '__main__':
    fork_lock = Lock()
    noodle_lock = Lock()
    Thread(target=eat1, args=('alex',)).start()
    Thread(target=eat2, args=('大壮',)).start()
    Thread(target=eat1, args=('wusir',)).start()
    Thread(target=eat2, args=('taibai',)).start()