# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 进程之间数据共康.py
# @datatime: 2023/4/30 10:44

"""
目标: 了解通过Multiprocessing模块的Manager类可以实现进程之间数据共享
由于进程之间数据共享是不安全的，需要加上互斥锁
Manager类对象可创建python所有数据类型
"""

from multiprocessing import Process, Manager, Lock, set_start_method

def change_data(dic, lock):
    with lock: # 加锁，保证数据安全
        dic['count'] -= 1

if __name__ == '__main__':
    set_start_method('fork') # 设置py开启进程方式为 'fork'
    m = Manager() # 创建Manager类对象
    lock = Lock()
    dic = m.dict({'count': 100}) # 创建字典
    p_lst = []
    for i in range(100):
        p = Process(target=change_data, args=(dic,lock))
        p.start()
        p_lst.append(p)
    for p in p_lst: p.join() # 异步阻塞
    print(dic)