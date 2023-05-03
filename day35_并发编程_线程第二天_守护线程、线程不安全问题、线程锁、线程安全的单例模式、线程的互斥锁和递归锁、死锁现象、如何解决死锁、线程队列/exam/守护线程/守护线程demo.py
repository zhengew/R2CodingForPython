# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 守护线程demo.py
# @datatime: 2023/5/1 09:09

"""
目标: 理解守护线程的守护范围
守护线程会守护其他子线程；
守护线程一致守护到主线程运行结束之后
"""
from threading import Thread, current_thread
import time
def func1():
    while True:
        print('%s: in func1' %current_thread().name, end=' ')
        time.sleep(1)
def func2():
    for i in range(2):
        print('%s: in func2' % current_thread().name, end=' ')
        time.sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.daemon = True # 守护线程
    t1.start()
    t2.start()
    t2.join() # 同步阻塞，等 t2执行结束后再往下执行
    print('主线程执行结束～')


