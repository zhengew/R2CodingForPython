# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: gevent模块实现的协程.py
# @datatime: 2023/5/3 16:03

"""
目标: 使用gevent模块实现协程
monkey和pach_all搭配使用，回重写部分内置模块
协程函数遇到阻塞事件才会切换，可以通过join主动阻塞来切换

"""
import gevent
from gevent import monkey
monkey.patch_all()
import time

def func1(t):
    print(t, ':start in func1')
    time.sleep(1)
    print('func1 end')
def func2(t):
    print(t, ':start in func2')
    time.sleep(1)
    print('func2 end')
    return t
if __name__ == '__main__':
    g1 = gevent.spawn(func1, time.time()) # 绑定协程函数，支持按位置参数或关键字参数传参
    g2 = gevent.spawn(func2, time.time())
    # g1.join() # 阻塞 直到g1协程任务执行结束
    # g2.join() # 阻塞 直到g2协程任务执行结束
    gevent.joinall((g1, g2)) # 等同于上面的分布阻塞





