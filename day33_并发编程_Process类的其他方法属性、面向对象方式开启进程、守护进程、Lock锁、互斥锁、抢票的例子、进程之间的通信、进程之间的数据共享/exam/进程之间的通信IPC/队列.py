# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 队列.py
# @datatime: 2023/4/29 12:46

"""
目标: 掌握通过队列实现进程之间的通信
set_start_method('fork') # 修改python进程启动方式为fork
注:mac系统默认进程启动方式为fork,python默认启动进程方式为spawn,两者不一致会抛异常
"""

from multiprocessing import Process, Queue, set_start_method
def consumer(q):
    while True:
        content = q.get()
        if content:
            print(content, end=' ')
        else:
            break
def producter(q):
    for i in range(1, 10):
        q.put(i)

if __name__ == '__main__':
    set_start_method('fork') # 修改python的进程启动方式为fork, 因为mac系统默认进程启动方式为fork,python默认启动进程方式为spawn
    q = Queue()
    p1 = Process(target=producter, args=(q,))
    p1.start()
    p2 = Process(target=consumer, args=(q,))
    p2.start()
    p1.join() # 主进程 同步阻塞，只有进程p1执行完毕，才继续往下执行
    q.put(None)



