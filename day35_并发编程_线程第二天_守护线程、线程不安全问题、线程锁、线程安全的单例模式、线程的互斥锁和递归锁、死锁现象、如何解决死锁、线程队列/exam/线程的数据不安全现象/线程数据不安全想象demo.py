# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 线程数据不安全想象demo.py
# @datatime: 2023/5/1 10:07

"""
目标:演示多线程操作全局变量产生的数据不安全现象
"""
from threading import Thread, current_thread
def add():
    global n
    for i in range(5000000):
        n += 1
def sub():
    global n
    for i in range(5000000):
        n -= 1
if __name__ == '__main__':
    n = 0
    t_lst = []
    for i in range(2):
        t1 = Thread(target=add)
        t2 = Thread(target=sub)
        t1.start()
        t2.start()
        t_lst.append(t1)
        t_lst.append(t2)

    for t in t_lst:
        t.join() # 异步阻塞
    print('主线程执行结束，全局变量n=%s' %n)
