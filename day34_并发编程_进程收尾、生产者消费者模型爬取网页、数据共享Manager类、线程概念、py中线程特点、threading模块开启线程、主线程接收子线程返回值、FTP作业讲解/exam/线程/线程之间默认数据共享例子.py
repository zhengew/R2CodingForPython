# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 线程之间默认数据共享例子.py
# @datatime: 2023/4/30 11:56

"""
目标: 线程之间数据共享例子
current_thread方法，获取当前线程对象
"""
from threading import Thread, Lock, current_thread
import time
def change_data(dic, lock):
    with lock:
        print(current_thread().ident, dic)
    dic['count'] -= 1

if __name__ == '__main__':
    dic = {'count': 100}
    t_lst = []
    lock = Lock()
    for i in range(5):
        t = Thread(target=change_data, args=(dic, lock))
        t.start()
        t_lst.append(t)

    for t in t_lst: t.join()
    print('主线程执行完毕，主进程中的dic:%s' %dic)



