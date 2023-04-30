# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 面向对象方式开启线程.py
# @datatime: 2023/4/30 12:11

"""
目标:掌握面向对象方式开启线程
enumerate方法，返回所有活着的线程对象，包含主线程，返回值是个列表
active_count方法：返回 enumerate方法返回值的长度，即所有活着的线程数
"""

from threading import Thread, current_thread, enumerate, active_count, Lock
import time
class MyThread(Thread):
    def __init__(self, num, lock):
        self.num = num
        self.lock = lock
        super().__init__()
    def run(self):
        with self.lock:
            self.num -= 1
        time.sleep(1)       # 睡1秒用来验证 enumerate 和 active_count方法
        print('当前线程对象:%s,num=%s\n' %(current_thread().name, self.num))
        return self.num     # 子线程结束后return返回值

if __name__ == '__main__':
    t_list = []
    num = 100
    lock = Lock()
    for i in range(10):
        t = MyThread(num, lock)
        t.start()
        num = t.num # 接收子线程返回值
        t_list.append(t)
    print('所有活着的线程对象:%s' % enumerate())
    print('活着的线程对象数量:%s' %active_count())
    for t in t_list: t.join() # 异步阻塞子线程
    print('主线程执行完毕，num = %s' %num)


