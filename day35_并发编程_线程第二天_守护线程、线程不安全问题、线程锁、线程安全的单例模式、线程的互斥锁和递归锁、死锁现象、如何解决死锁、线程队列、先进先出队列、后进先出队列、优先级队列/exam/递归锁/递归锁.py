# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 递归锁.py
# @datatime: 2023/5/1 12:56

"""
目标:掌握递归锁
递归锁可以在同一个线程被acquire和release多次；
递归锁 acquire多少次，就需要release多少次，否则会进入阻塞状态，其他线程也拿不到最外层的锁
"""

from threading import Thread, RLock

def func(lock):
    lock.acquire()
    lock.acquire()
    print('start~')
    lock.release()
    # lock.release() # 递归锁 少release一次，当前子进程执行完毕，其他子进程也拿不到最外层的钥匙，进入阻塞状态
    print('end~')

if __name__ == '__main__':
    lock = RLock()
    for i in range(2):
        Thread(target=func, args=(lock,)).start()
