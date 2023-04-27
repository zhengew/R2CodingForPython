# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: multiprocessing_demo1.py
# @datatime: 2023/4/27 下午2:35

"""
目标: 掌握 multiprocessing模块 多元的处理进程
只会在主进程中执行的代码写在 if __name__ == '__main__'下：
原因：
1.在win和部分mac系统中，子进程会导入主进程中的所有成员，
但在导入模块时__name__ == 被导入的模块名，所以子进程不会导入__main__下的代码，
2.在linux系统中会完全fork一份主进程内存空间中的成员内存地址
"""
from multiprocessing import Process

n = 0
def func(n):
    n += 1
    print('子进程:', n)

if __name__ == '__main__':
    for i in range(4):
        p = Process(target=func, args=(n, ))
        p.start()
    print('主进程:', n) # 0
