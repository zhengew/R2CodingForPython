# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 队列实现生产者消费着模型.py
# @datatime: 2023/4/29 16:46

"""
目标: 了解生产者与消费者模型
本质就是让生产数据和消费数据的效率达到平衡并最大化效率
consumer: 消费者
producer: 生产者
"""

from multiprocessing import Process, Queue, set_start_method
import time
import random
def consumer(name, q): # 消费者在拿到数据后通常要进行某处处理操作
    while True:
        foodi = q.get() # 因为消费者get队列的长度不固定，所以需要与生产者约定终止条件，本案例中的终止条件为None
        if foodi:
            print('%s吃了%s' %(name, foodi))
        else:
            break
def producer(name, food, q): # 生产者在存放数据之前通常要先通过代码来获取指定数据
    for i in range(3):
        foodi = '%s%s' %(food, i)
        print('%s生产了%s~' %(name, foodi))
        time.sleep(random.random())
        q.put(foodi)


if __name__ == '__main__':
    set_start_method('fork') # 进程开启方式 fork
    q = Queue()
    p1 = Process(target=producer, args=('alex', '泔水',q))
    p2 = Process(target=producer, args=('taibai', '香蕉',q))
    p3 = Process(target=consumer, args=('wusir', q))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    q.put(None) # 注意：有几个消费者就需要put几个None来终止消费




























