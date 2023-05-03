# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 通过递归锁解决死锁.py
# @datatime: 2023/5/1 13:56

"""
目标: 掌握递归锁解决死锁问题
将所有的互斥锁都编程一把递归锁
"""
from threading import Thread, RLock as Lock # 将原本的互斥锁改成递归锁
import time
def eat1(name):
    fork_noodle_lock.acquire()
    print(name, '抢到叉子～')
    print(name, '抢到面～')
    print(name, '开始吃面～')
    time.sleep(0.1)
    fork_noodle_lock.release()
    print(name,'放下面~')
    print(name, '放下叉子')
def eat2(name):
    fork_noodle_lock.acquire()
    print(name, '抢到面～')
    print(name, '抢到叉子～')
    print(name, '开始吃面～')
    time.sleep(0.1)
    fork_noodle_lock.release()
    print(name, '放下叉子')
    print(name,'放下面~')

if __name__ == '__main__':
    fork_noodle_lock = fork_lock = noodle_lock = Lock() # 将所有的锁都改成一把递归锁

    Thread(target=eat1, args=('alex',)).start()
    Thread(target=eat2, args=('大壮',)).start()
    Thread(target=eat1, args=('wusir',)).start()
    Thread(target=eat2, args=('taibai',)).start()